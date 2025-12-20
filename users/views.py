from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views import View

from myapp.models import Food
from .forms import CustomUserCreationForm, ProfileUpdateForm  # UserForm emas, biz yozgandek
from django.contrib.auth import update_session_auth_hash

from .models import Comment


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



def add_comment(request, food_id):
    if request.method == 'POST':
        food = get_object_or_404(Food, id=food_id)
        Comment.objects.create(
            food=food,
            user=request.user,
            text=request.POST.get('text')
        )
    return redirect('users:profile')

def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    if request.method == 'POST':
        comment.text = request.POST.get('text')
        comment.save()
        return redirect('users:profile')
    return render(request, 'users/edit_comment.html', {'comment': comment})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    comment.delete()
    return redirect('users:profile')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('myapp:home_page')

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


@login_required
def profile_view(request):
    user = request.user
    comments = Comment.objects.filter(user=user)
    foods = Food.objects.filter(user=user)
    return render(request, 'users/profile.html', {
        'user': user,
        'comments': comments,
        'foods': foods
    })