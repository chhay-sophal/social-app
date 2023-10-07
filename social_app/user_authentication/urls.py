from django.urls import path
from .views import *

app_name = 'user_authentication'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
]