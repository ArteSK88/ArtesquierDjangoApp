from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('categories', views.categories, name='categories'),
    path('categories/<int:id>/<slug:slug>', views.menus, name='menus')
]
