from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import ProfileForm, ProfileUpdateForm
from user_authentication.models import Profile

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user_profile/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profiles = Profile.objects.all()
        context['profiles'] = profiles
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProfileUpdateForm
    template_name = 'user_profile/profile_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user.profile