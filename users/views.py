from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.views import View
from .forms import CustomUserCreationForm  # UserForm emas, biz yozgandek

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
        return redirect('register')
