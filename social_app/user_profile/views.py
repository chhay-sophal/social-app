from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import UserProfileForm, UserForm, ProfilePictureForm
from user_authentication.models import Profile
from posts.models import Post

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user_profile/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        context['posts'] = user.posts.all()  # Access the posts through the related_name 'posts'
        return context

    
class ProfileUpdateView(LoginRequiredMixin, FormView):
    template_name = 'user_profile/profile_update.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('user_profile:profile')

    def get(self, request, *args, **kwargs):
        user = request.user
        profile = user.profile
        user_form = UserForm(instance=user)
        profile_form = UserProfileForm(instance=profile)
        return self.render_to_response({'user_form': user_form, 'profile_form': profile_form})

    def form_valid(self, form):
        user = self.request.user
        profile = user.profile
        user_form = UserForm(self.request.POST, instance=user)
        profile_form = UserProfileForm(self.request.POST, instance=profile)
        if user_form.is_valid():
            user_form.save()
        if profile_form.is_valid():
            profile_form.save()
        form.instance = profile
        form.save()
        return super().form_valid(form)
    
class ChangeProfilePictureView(LoginRequiredMixin, View):
    form_class = ProfilePictureForm
    template_name = 'user_profile/change_profile.html'
    success_url = 'user_profile:profile'

    def get(self, request, *args, **kwargs):
        user = request.user
        profile = user.profile
        form = self.form_class(instance=profile)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        user = request.user
        profile = user.profile
        form = self.form_class(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})