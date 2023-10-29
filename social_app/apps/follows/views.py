from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Follow


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'follows/user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        current_user = self.request.user

        # Exclude users that the current user is already following
        queryset = User.objects.exclude(id__in=Follow.objects.filter(from_user=current_user).values('to_user'))

        # Exclude the superuser from the queryset
        queryset = queryset.exclude(is_superuser=True)

        # Exclude the current user from the queryset
        queryset = queryset.exclude(id=current_user.id)

        return queryset


class FollowingListView(LoginRequiredMixin, ListView):
    model = Follow
    template_name = 'follows/following_list.html'
    context_object_name = 'following'
    extra_context = {}

    def get_queryset(self):
        current_user = self.request.user
        queryset = Follow.objects.filter(from_user=current_user)
        self.extra_context['following_count'] = queryset.count()
        return queryset
    

class FollowerListView(LoginRequiredMixin, ListView):
    model = Follow
    template_name = 'follows/follower_list.html'
    context_object_name = 'followers'
    extra_context = {}
    
    def get_queryset(self):
        current_user = self.request.user
        queryset = Follow.objects.filter(to_user=current_user)
        self.extra_context['followers_count'] = queryset.count()
        return queryset
    

class FollowUserView(LoginRequiredMixin, View):
    def post(self, request):
        from_user_id = request.POST.get('from_user_id')
        to_user_id = request.POST.get('to_user_id')

        # Create a new entry in the Follow model
        follow = Follow.objects.create(
            from_user_id=from_user_id,
            to_user_id=to_user_id
        )

        return redirect('follows:user-list')  # Redirect to the recommend page after following


class UnfollowUserView(LoginRequiredMixin, View):
    def post(self, request):
        from_user_id = request.POST.get('from_user_id')
        to_user_id = request.POST.get('to_user_id')

        # Retrieve the Follow object and delete it
        try:
            follow = Follow.objects.get(from_user_id=from_user_id, to_user_id=to_user_id)
            follow.delete()
        except Follow.DoesNotExist:
            pass

        return redirect('follows:following-list')
    
class RemoveFollowerView(View):
    def post(self, request):
        from_user_id = request.POST.get('from_user_id')
        to_user_id = request.POST.get('to_user_id')

        # Retrieve the Follow object and delete it
        try:
            follow = Follow.objects.get(from_user_id=from_user_id, to_user_id=to_user_id)
            follow.delete()
        except Follow.DoesNotExist:
            pass

        return redirect('follows:follower-list')