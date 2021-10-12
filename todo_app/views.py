from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by("-added_date") #newest date to oldest date
    return render(request, 'todo_app/home.html', {'todo_items':todo_items})

@csrf_exempt
def add_todo(request):
    print(request.POST)
    current_date = timezone.now()
    content = request.POST["content"]
    created_object = Todo.objects.create(added_date=current_date,text=content) # creates database entry

    length_of_todos = Todo.objects.all().count()

    print(length_of_todos)
    print(created_object.id)
    # return render(request, 'todo_app/home.html')
    # direct to home page instead of render. thats why objects dont show up
    # they are not being passed in
    return HttpResponseRedirect("/")


@csrf_exempt
def delete(request, todo_id):
    print(todo_id)
    Todo.objects.get(id=todo_id).delete()
    
    return HttpResponseRedirect("/")
