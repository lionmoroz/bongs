from django import forms
from .models import Order 


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'area','nova_city', 'nova_warehouse']

