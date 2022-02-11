from django.shortcuts import render, redirect
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages

# adding and showing tasks.
def todolist(request):
    if request.method == "POST":
        form= TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,("new task added!"))
        return redirect('todolist')
    else:
        all_tasks  = TaskList.objects.all
        return render(request, 'todolist.html', {'all_tasks': all_tasks})

#contact page
def contact(request):
    context = {
        'contact_text': "welcome to contact page.",
        }
    return render(request, 'contact.html', context)

#about page
def about(request):
    context = {
        'about_text': "welcome to about page.",
        }
    return render(request, 'about.html', context)

#delete a task
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')
    
#edit task
def edit_task(request, task_id):
    if request.method == "POST":
        
        messages.success(request,("task edited!"))
        return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})