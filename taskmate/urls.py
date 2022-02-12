from django.contrib import admin
from django.urls import path, include
from todolist_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('todolist_app.urls')), #this redirects to our todolist_app urls funct
    path('contact', views.contact, name= 'contact'),
    path('about', views.about, name= 'about'),
    path('', views.index, name="index"),
]
