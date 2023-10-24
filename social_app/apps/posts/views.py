from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Post, Like
from apps.user_authentication.models import Profile
from apps.follows.models import Follow
from .forms import *


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
        else:
            # User has not liked the post, handle like action
            like = Like(user=user, post=post)
            like.save()

        return redirect('posts:home')