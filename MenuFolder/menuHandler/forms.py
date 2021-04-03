from django.forms import BaseModelForm
from django import forms


class CreateNewRestaurantForm(forms.Form):

    def clean(self):
        restaurant_name = self.cleaned_data.get('name')
        rest_phone = self.cleaned_data.get('phone')
        address = self.cleaned_data.get('address')
        city = self.cleaned_data.get('city')
        state = self.cleaned_data.get('state')
        zip_code = self.cleaned_data.get('zip')
