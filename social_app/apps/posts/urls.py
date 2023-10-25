from django.urls import path
from .views import *
from . import views

app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/like/', PostLikeView.as_view(), name='post_like'),
    path('post/get_comments/', GetCommentsView.as_view(), name='get_comments'),
    path('post/comment/', PostCommentView.as_view(), name='post_comment'),
]