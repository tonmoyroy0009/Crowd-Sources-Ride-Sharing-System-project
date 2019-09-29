from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='createCycle'),
    path('<int:id>', views.cycleView, name='cycleView'),
    path('update/<int:id>', views.update, name='updateCycle'),
    path('delete/<int:id>', views.delete, name='deleteCycle'),
    path('pickcycle/<int:id>', views.pickcycle, name='pickcycle'),
]
