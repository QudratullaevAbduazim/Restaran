from django.urls import path
from .views import home_page, FoodCreateView, FoodUpdateView, FoodDeleteView



app_name = 'myapp'

urlpatterns = [
    path('', home_page, name='home_page'),
    path('create-food/', FoodCreateView.as_view(), name='create_food'),
    path('update-food/<int:pk>/', FoodUpdateView.as_view(), name='update_food'),
    path('delete-food/<int:pk>/', FoodDeleteView.as_view(), name='delete_food'),
]
