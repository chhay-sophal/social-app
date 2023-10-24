from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from apps.user_authentication.models import Profile
from .forms import *


class PostListView(LoginRequiredMixin, ListView):
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 10  # Number of posts to display per page

    def get_queryset(self):
        # Get all posts ordered by created_at in descending order
        posts = Post.objects.order_by('-created_at')
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