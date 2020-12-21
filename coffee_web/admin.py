from django.contrib import admin
from coffee_web.models import Coffee, OrderCoffee, OrderCoffeeList


@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    list_display =('id', 'name', 'slug', 'price', 'measure', 'description')
    search_fields = ['id', 'name', 'slug', 'price', 'description']
    list_filter = ['id', 'name', 'slug', 'price', 'description']

@admin.register(OrderCoffee)
class OrderCoffeeAdmin(admin.ModelAdmin):
    list_display =('id', 'first_name', 'last_name', 'email', 'address', 'city')
    search_fields = ['id', 'first_name', 'last_name', 'email', 'address', 'city']
    list_filter = ['id', 'first_name', 'last_name', 'email', 'address', 'city']

@admin.register(OrderCoffeeList)
class OrderCoffeeListAdmin(admin.ModelAdmin):
    list_display =('id', 'order_id', 'coffee', 'measure', 'quantity', 'sum_price', 'created', 'paid')
    search_fields = ['id', 'created', 'paid']
    list_filter = ['id', 'created', 'paid']

