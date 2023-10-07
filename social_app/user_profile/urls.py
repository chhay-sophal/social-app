from django.urls import path
from .views import *

app_name = 'user_profile'

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
]