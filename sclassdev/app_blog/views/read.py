from django.shortcuts import render
from app_blog.utility import query

def view(request, id):
    if request.method == 'GET':
        post = query("SELECT * FROM blog_post WHERE id=%s", [id])
        if post :
            post = post[0]
            return render(request, 'app_blog/read.html',{
            'post':post
            })
        else :
            return render(request, 'app_blog/notfound.html',status=404)