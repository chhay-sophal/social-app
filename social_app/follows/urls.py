from django.urls import path
from .views import UserListView, FollowUserView, FollowingListView, UnfollowUserView, FollowerListView, RemoveFollowerView

app_name = 'follows'

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('follow/', FollowUserView.as_view(), name='follow-user'),
    path('following/', FollowingListView.as_view(), name='following-list'),
    path('unfollow/', UnfollowUserView.as_view(), name='unfollow-user'),
    path('followers/', FollowerListView.as_view(), name='follower-list'),
    path('remove-follower/', RemoveFollowerView.as_view(), name='remove-follower'),
]