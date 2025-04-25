
from django.urls import path
from app_blog.views import create

urlpatterns = [
    path('create/', create.view, name='create')
]