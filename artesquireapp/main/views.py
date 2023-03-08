from django.shortcuts import render, redirect
from .models import *


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница сайта'})

def categories(request):
    categories = Category.objects.all()
    context = {'title': 'Меню', 'categories': categories}
    return render(request, 'main/categories.html', context)

def menus(request, id, slug):
    categories = Category.objects.all()
    context = {'title': 'Обзор меню', 'categories': categories, 'category_id': id}
    return render(request, 'main/menus.html', context)