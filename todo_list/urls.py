from django . urls import path
from . import views



urlpatterns =[
    path('', views.task, name='task'),
    path('update/<str:i>/', views.update_list, name='update'),
    path('delete/<str:i>/', views.deleteTask, name='delete'),
]