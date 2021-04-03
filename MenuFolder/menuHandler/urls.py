from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('/restaurants', views.restaurants, name='restaurants'),
    path('/user_restaurants', views.user_restaurants, name='user_restaurants'),
    path('/add_restaraurant', views.add_restaurant, name='add_restaurant'),
    path('/your-restaurant<int:restaurant_id>', views.restaurant_page_view, name='restaurant_page'),
    path('/new_menu<int:restaurant_id>', views.new_menu, name='new_menu'),
]