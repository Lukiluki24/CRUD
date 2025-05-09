from django.shortcuts import render, redirect
from app_blog.utility import query

def view(request,id):
    post = query("SELECT * FROM blog_post WHERE id=%s", [id])
    
    if request.method == 'POST':
        if not post :
            return render(request, 'app_blog/notfound.html',status=404)
        
        post = post[0]

        newTitle = request.POST.get('title')
        newContent = request.POST.get('content')

        result = query("UPDATE blog_post SET title=%s, content=%s WHERE id=%s", 
                       [newTitle, newContent, id])

        return redirect(f'/blog/read/{id}')
    
    return render(request, 'app_blog/update.html', {'post':post})