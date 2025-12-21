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




class DeleteCommentView(LoginRequiredMixin, View):
    def get(self, request, pk):
        comment = get_object_or_404(Comment, id=pk, user=request.user)
        comment.delete()
        return redirect('myapp:home_page')


class CommentUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        comment = get_object_or_404(Comment, id=pk, user=request.user)
        return render(request, 'users/update_comment.html', {'comment': comment})

    def post(self, request, pk):
        comment = get_object_or_404(Comment, id=pk, user=request.user)
        new_text = request.POST.get('text')

        if new_text:
            comment.text = new_text
            comment.save()
            return redirect('myapp:home_page')

        return render(request, 'users/update_comment.html', {'comment': comment})


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


def profile_view(request):
    user = request.user
    my_comments = Comment.objects.filter(user=user).order_by('-id')
    my_foods = Food.objects.filter(user=user).order_by('-id')
    return render(request, 'users/profile.html', {
        'user': user,
        'my_comments': my_comments,
        'my_foods': my_foods
    })

