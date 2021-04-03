from django.contrib import admin
from menuHandler.models import Restaurant

class RestaurantAdmin():
    ...

class MenuAdmin():
    ...

class FoodItemAdmin():
    ...

# Register your models here.
admin.site.register(Restaurant)