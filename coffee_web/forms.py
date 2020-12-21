from django import forms
from django.forms import fields

# from django.forms import forms
from coffee_web.models import Coffee, OrderCoffee, OrderCoffeeList

class CoffeeForm(forms.ModelForm):
    class Meta: 
        model= Coffee
        fields=['name', 'measure', 'price']
        widgets ={
            'name': forms.Select(attrs={'class': 'form-control'}),
            'measure': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.Select(attrs={'class': 'form-control'})
        }

      
class OrderCoffeeForm(forms.ModelForm):
    class Meta:
        model= OrderCoffee
        fields ='__all__'
        widgets ={
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'address' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'address'}),
            'city' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'city'}),
            
        }


class OrderCoffeeListForm(forms.ModelForm):
    class Meta:
        model = OrderCoffeeList
        fields = '__all__'
        widgets ={
            'coffee': forms.Select(attrs={'class': 'form-control'}),
            'quantity':forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'quantity'}),
            'paid': forms.CheckboxInput(attrs={'class': 'form-control'})
        }


        