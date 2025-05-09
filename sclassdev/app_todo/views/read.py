from django.shortcuts import render
from app_todo.utility import query

def view(request, id):
    if request.method == 'GET':
        post = query("SELECT * FROM todo_post WHERE id=%s", [id])
        if post :
            post = post[0]
            return render(request, 'app_todo/read.html',{
            'post':post
            })
        else :
            return render(request, 'app_todo/notfound.html',status=404)