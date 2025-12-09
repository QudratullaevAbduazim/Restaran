from django.db import models
from django.shortcuts import render
from django.urls import reverse_lazy

from . import models
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import FoodForm
from .models import Food


# Create your views here.

def home_page(request):
    foods = models.Food.objects.all().order_by('-id')
    context = {'foods': foods}
    return render(request, 'home.html', context)

class FoodCreateView(CreateView):
    model = Food
    form_class = FoodForm
    template_name = 'create_food.html'
    success_url = reverse_lazy('myapp:home_page')
class FoodUpdateView(UpdateView):
    model = Food
    form_class = FoodForm
    template_name = 'update_food.html'
    success_url = reverse_lazy('myapp:home_page')
class FoodDeleteView(DeleteView):
    model = Food
    template_name = 'delete_food.html'
    success_url = reverse_lazy('myapp:home_page')