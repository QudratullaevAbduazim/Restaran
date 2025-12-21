from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View

from users.models import Comment
from . import models
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import FoodForm
from .models import Food


# Create your views here.

class HomeView(View):

    def get(self, request):
        foods = Food.objects.all().order_by('-id')
        return render(request, 'home.html', {'foods': foods})

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('users:login')

        food_id = request.POST.get('food_id')
        text = request.POST.get('text')

        if food_id and text:
            food = get_object_or_404(Food, id=food_id)
            Comment.objects.create(
                user=request.user,
                food=food,
                text=text
            )

        return redirect('myapp:home_page')


class FoodCreateView(View):
    def get(self, request):
        form = FoodForm()
        return render(request, 'create_food.html', {'form': form})

    def post(self, request):
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            food = form.save(commit=False)
            food.user = request.user
            food.save()
            return redirect('myapp:home_page')
        return render(request, 'create_food.html', {'form': form})


class FoodUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        food = get_object_or_404(Food, pk=pk, user=request.user)
        form = FoodForm(instance=food)
        return render(request, 'update_food.html', {'form': form, 'food': food})

    def post(self, request, pk):
        food = get_object_or_404(Food, pk=pk, user=request.user)
        form = FoodForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
        return render(request, 'update_food.html', {'form': form, 'food': food})


class FoodDeleteView(DeleteView):
    model = Food
    template_name = 'delete_food.html'
    success_url = reverse_lazy('myapp:home_page')