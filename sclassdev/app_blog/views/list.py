from django.shortcuts import render
from app_blog.utility import query

def view(request):
    if request.method == 'GET':
        posts = query("SELECT * FROM blog_post ORDER BY id DESC")

    return render(request, 'app_blog/list.html',{
        'posts':posts
    })