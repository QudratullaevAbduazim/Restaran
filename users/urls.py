from django.urls import path
from .views import RegisterView, ProfileView, LogoutView, change_password, ProfileUpdateView, login_view, add_comment, \
    edit_comment, delete_comment

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-pass/', change_password, name='change-pass'),
    path('update-profile/', ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('comment/add/<int:food_id>/', add_comment, name='add_comment'),
    path('comment-update/<int:food_id>/', edit_comment, name='update_comment'),
    path('comment-update/<int:food_id>/', delete_comment, name='del_comment'),
]
