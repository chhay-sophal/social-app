from django.urls import path
from .views import *

app_name = 'user_profile'

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('modify_profile/', ProfileUpdateView.as_view(), name='profile_update'),
    path('change_profile_picture/', ChangeProfilePictureView.as_view(), name='change_profile'),
]