from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import RegistrationForm, LoginForm, ProfileForm, ProfileUpdateForm
from .models import Profile


class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'user_authentication/register.html'
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    template_name = 'user_authentication/login.html'
    authentication_form = LoginForm


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user_authentication/profile.html'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProfileUpdateForm
    template_name = 'user_authentication/profile_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user.profile