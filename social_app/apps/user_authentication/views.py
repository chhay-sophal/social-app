from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import RegistrationForm, LoginForm
from .models import Profile


class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'user_authentication/register.html'
    success_url = reverse_lazy('user_auth:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        Profile.objects.create(user=self.object, name=name, email=email)
        return response


class CustomLoginView(LoginView):
    template_name = 'user_authentication/login.html'
    success_url = 'user_profile'


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('user_auth:login')

class CustomPasswordChangeView(PasswordChangeView):
    template_name = "user_authentication/password_change.html"
    success_url = reverse_lazy('user_auth:logout')