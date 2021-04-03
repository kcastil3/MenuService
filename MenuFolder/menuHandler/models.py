from django.db import models
from menuHandler.managers import RestaurantManager, MenuManager, FoodManager

# Create your models here.
class Restaurant(models.Model):
    restaurant_id = models.IntegerField(primary_key=True)
    associated_user = models.CharField(max_length=30)
    restaurant_name = models.CharField(max_length=30)
    rest_phone = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length =2)
    zip_code = models.CharField(max_length=5)

    photo_main = models.ImageField(null=True, blank=True)
    
    open_time = models.TimeField(null=True, blank=True) #TODO need to make different open/close for every day of the week
    close_time = models.TimeField(null=True, blank=True)

    
    delivery_available = models.BooleanField(null=True, blank=True)
    delivery_range = models.IntegerField(null=True, blank=True)
    pay_in_person = models.BooleanField(null=True, blank=True)

    contact_first_name = models.CharField(max_length=20, null=True, blank=True)
    contact_last_name =models.CharField(max_length=20, null=True, blank=True)
    contact_phone = models.CharField(max_length=10, null=True, blank=True)

    objects = RestaurantManager()

    #TODO add links to social media :(


class Menu(models.Model):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)  # Links menu to a restaurant
    menu_category = models.CharField(max_length=20)


class FoodItem(models.Model):
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    
    description = models.CharField(max_length=100)
    price = models.FloatField()
    photo = models.ImageField()
    