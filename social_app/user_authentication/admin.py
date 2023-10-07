from django.contrib import admin
from .models import Profile
# Register your models here.
@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'bio', 'profile_picture')