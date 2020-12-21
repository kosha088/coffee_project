from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone


class Coffee(models.Model):
    MEASURE =[
        ('250 ml', '250 ml'),
        ('500 ml', '500 ml'),
        ('700 ml', '700 ml')
    ]
    name = models.CharField(max_length=255, verbose_name='Название', db_index=True)
    slug = models.CharField(max_length=255, db_index=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    measure = models.CharField(max_length=255, choices=MEASURE, default='500mg', verbose_name='Мера')
    
    class Meta:
        ordering =['id']
        verbose_name ='Кофе'
        verbose_name_plural ='Список кофе'
    
    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('coffee', kwargs={"id": self.pk})


class OrderCoffee(models.Model):
    CITY=[
        ('Kzo', 'Kyzylorda')
    ]
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    email = models.EmailField()
    address = models.CharField(max_length=255, verbose_name='Адрес')
    city = models.CharField(max_length=255, verbose_name='Город', choices=CITY, default='Kzo')
    

    class Meta:
        ordering = ['id']
        verbose_name = 'Заказчик кофе'
        verbose_name_plural='Заказчики кофе'
    
    def __str__(self):
        return f'Заказчик: {self.id} {self.first_name} {self.email}'

class OrderCoffeeList(models.Model):
    order = models.ForeignKey(OrderCoffee, related_name='order_coffee', on_delete=models.CASCADE, default=1, verbose_name='Заказ')
    coffee = models.ForeignKey(Coffee, related_name='coffee', on_delete=models.CASCADE, default=1, verbose_name='Кофе')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    created = models.DateTimeField(auto_now_add=timezone.now(), verbose_name='Дата создания')
    paid = models.BooleanField(default=False, verbose_name='Оплата', blank=True, null=True)
 
    class Meta:
        verbose_name = 'Лист заказов'
        verbose_name_plural = ' Листы заказов'
        ordering = ['-created']

    def __str__(self):
        return f'Номер заказа {self.id}'
    
    def sum_price(self):
        return self.coffee.price * self.quantity

    def measure(self):
        return self.coffee.measure









