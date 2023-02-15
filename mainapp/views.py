from re import template
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import *


class HomeView(ListView):
    template_name = 'index.html'
    model = Category
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["covers"] = Cover.objects.all()
        return context


def food_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    food_items = FoodModel.objects.filter(category=category)
    context = {'category': category, 'food_items': food_items,
               'covers': Cover.objects.all()}
    return render(request, 'fruit.html', context)
