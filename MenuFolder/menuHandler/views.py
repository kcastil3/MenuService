from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from menuHandler.forms import CreateNewRestaurantForm
from menuHandler.models import Restaurant, Menu, FoodItem
from menuHandler.managers import RestaurantManager, MenuManager, FoodManager

# Create your views here.
def restaurants(request):
    return render(request, 'restaurants.html')


def user_restaurants(request):
    restaurants = Restaurant.objects.filter(associated_user=request.user)
    context = {
        'restaurants': restaurants
    }
    return render(request, 'user_restaurants.html', context)


def add_restaurant(request):
    if request.method == 'POST':
        form = CreateNewRestaurantForm(request.POST)
        if form.is_valid():
            form.clean()
            name = request.POST['name']
            address = request.POST['address']
            city = request.POST['city']
            zipcode = request.POST['zipcode']
            email = request.POST['email']
            phone = request.POST['phone']
            Restaurant.objects.create(associated_user=request.user, restaurant_name=name, address=address, city=city, zip_code=zipcode, rest_phone=phone)
            #TODO Create Managers for Restaurants, and menus.   
            #TODO need to fix the html endings for scalability!!!
            return render(request, 'user_restaurants.html')
    elif request.method == 'GET':
        return render(request, 'add_restaurant.html')


def restaurant_page_view(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    context = {
        'restaurant': restaurant
    }

    return render(request, 'restaurant_page.html', context)

def new_menu(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    context = {
        'restaurant': restaurant
    }

    return render(request, 'new_menu.html', context)
