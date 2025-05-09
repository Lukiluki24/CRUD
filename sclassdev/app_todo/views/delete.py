from django.shortcuts import render, redirect
from app_todo.utility import query

def view(request, id):
    if request.method == 'GET':
        post = query("DELETE FROM todo_post WHERE id=%s", [id])
        
    return redirect('/todo/list/', name='todo_list')