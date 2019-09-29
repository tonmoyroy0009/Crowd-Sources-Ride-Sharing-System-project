from django.urls import path
from . import views

urlpatterns = [
    path('balance/', views.balance, name='balance'),
    path('transition/<int:id>', views.transition, name='transition'),
    path('cash/', views.cash, name='cash'),
] 
