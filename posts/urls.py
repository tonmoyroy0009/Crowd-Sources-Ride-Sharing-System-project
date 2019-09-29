from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='post'),
    path('create/', views.createPost, name='createPost'),
    path('<int:id>', views.detail, name='detail'),
    path('update/<int:id>', views.update, name='updatePost'),
    path('delete/<int:id>', views.delete, name='deletePost'),
] 
