from django.urls import path
from .views import RegisterView, LogoutView, change_password, ProfileUpdateView, DeleteCommentView, \
    login_view, profile_view, CommentUpdateView

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-pass/', change_password, name='change-pass'),
    path('update-profile/', ProfileUpdateView.as_view(), name='profile_update'),
    path('comment-update/<int:pk>/', CommentUpdateView.as_view(), name='update_comment'),
    path('delete-comment/<int:pk>/', DeleteCommentView.as_view(), name='delete_comment'),
]
