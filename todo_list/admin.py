from django.contrib import admin
from django.urls import path, include

# Register your models here.
from . models import *
admin . site. register(Task)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_list.urls')),
]