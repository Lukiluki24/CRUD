from django.shortcuts import render, redirect
from app_todo.utility import query

def view(request,id):
    post = query("SELECT * FROM todo_post WHERE id=%s", [id])
    
    if request.method == 'POST':
        if not post :
            return render(request, 'app_todo/notfound.html',status=404)
        
        post = post[0]

        newTitle = request.POST.get('title')
        newContent = request.POST.get('content')

        result = query("UPDATE todo_post SET title=%s, content=%s WHERE id=%s", 
                       [newTitle, newContent, id])

        return redirect(f'/todo/read/{id}')
    
    return render(request, 'app_todo/update.html', {'post':post})