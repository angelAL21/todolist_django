from django.shortcuts import render

# Create your views here.

def todolist(request):
    context = {
        'welcome_text': "welcome ToDo list page",
        }
    return render(request, 'todolist.html', context)

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