from django.shortcuts import render
from app_todo.utility import query

def view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        result = query("INSERT INTO todo_post (title, content) VALUES (%s, %s)", [title, content])
        print(result)

    return render(request, 'app_todo/create.html')