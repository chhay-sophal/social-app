from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register')
]