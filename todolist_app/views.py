from django.shortcuts import render, redirect
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm

# Create your views here.
def todolist(request):
    if request.method == "POST":
        form= TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('todolist')
    else:
        all_tasks  = TaskList.objects.all
        return render(request, 'todolist.html', {'all_tasks': all_tasks})

def contact(request):
    context = {
        'contact_text': "welcome to contact page.",
        }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'about_text': "welcome to about page.",
        }
    return render(request, 'about.html', context)