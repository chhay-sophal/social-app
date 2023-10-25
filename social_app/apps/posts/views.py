from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from .models import Post, Like, Comment
from apps.user_authentication.models import Profile
from apps.follows.models import Follow
from .forms import *
from .serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class PostListView(LoginRequiredMixin, ListView):
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 10  # Number of posts to display per page

    def get_queryset(self):
        # Get the current user
        user = self.request.user

        # Get the authors that the current user is following
        following_authors = Follow.objects.filter(from_user=user).values_list('to_user', flat=True)

        # Retrieve posts from the following authors and the current user
        posts = Post.objects.filter(Q(author__in=following_authors) | Q(author=user)).order_by('-created_at')

        return posts


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/post_create.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('posts:home')
    

class PostLikeView(View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        if user in post.likes.all():
            # User has already liked the post, handle unlike action
            like = Like.objects.get(user=user, post=post)
            like.delete()
            liked = False
        else:
            # User has not liked the post, handle like action
            like = Like(user=user, post=post)
            like.save()
            liked = True

        response_data = {
            'like_count': post.likes.count(),
            'button_text': 'Unlike' if liked else 'Like'
        }

        return JsonResponse(response_data)


class PostCommentView(APIView):
    def post(self, request):
        post_id = request.data.get('post_id')
        content = request.data.get('content')
        # Create the comment
        comment = Comment.objects.create(post_id=post_id, user=request.user, content=content)
        # Serialize the comment
        serializer = CommentSerializer(comment)
        # Return the serialized comment as JSON response
        return Response({'comment': serializer.data})
    
    
class GetCommentsView(APIView):
    def get(self, request):
        post_id = request.GET.get('post_id')
        comments = Comment.objects.filter(post_id=post_id)
        serialized_comments = CommentSerializer(comments, many=True).data
        comments_html = render_to_string('posts/comments.html', {'comments': serialized_comments})
        return Response({'comments_html': comments_html})