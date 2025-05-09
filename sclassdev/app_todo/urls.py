
from django.urls import path
from app_todo.views import create, list, read, delete, update

urlpatterns = [
    path('create/', create.view, name='create'),
    path('list/', list.view, name='list'),
    path('read/<int:id>/', read.view, name='read'),
    path('delete/<int:id>/', delete.view, name='delete'),
    path('update/<int:id>/', update.view, name='update')
]