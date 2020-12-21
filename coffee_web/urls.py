from django.urls import path, include
from coffee_web import views_cbv
from coffee_web import views

urlpatterns =[
    # path('', views_cbv.IndexView.as_view(), name='main'),
    # path('create', views_cbv.CreateOrderView.as_view(), name='create')
    path('', views.index, name='main'),
    path('create', views.create, name='create'),

]