from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import View
from .forms import CustomUserCreationForm, ProfileUpdateForm  # UserForm emas, biz yozgandek
from django.contrib.auth import update_session_auth_hash
class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('myapp:home_page')
        return render(request, 'users/register.html', {'form': form})


class ProfileView(View):
    def get(self, request):
        user = request.user
        return render(request, 'users/profile.html', {'user': user})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('myapp:home_page')



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('users:profile')
        else:
            messages.error(request, 'Username yoki parol noto‘g‘ri')
    return render(request, 'users/login.html')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('users:profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {'form': form})



class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        form = ProfileUpdateForm(instance=request.user)
        return render(request, 'users/profile_update.html', {'form': form})

    def post(self, request):
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('myapp:home_page')
        return render(request, 'users/profile_update.html', {'form': form})



