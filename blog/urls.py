from django.urls import path, include
from blog import views

urlpatterns =[
    path('blog', views.blog, name='blog'),
    path('<int:id>/', views.detail, name='detail')
]