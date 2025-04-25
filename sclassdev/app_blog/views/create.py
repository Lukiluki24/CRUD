from django.shortcuts import render
from app_blog.utility import query

def view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        result = query("INSERT INTO blog_post (title, content) VALUES (%s, %s)", [title, content])
        print(result)

    return render(request, 'app_blog/create.html')