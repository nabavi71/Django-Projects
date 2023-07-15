from django.urls import path
from .views import homeView, todoListView, todoTaskCreate, todoTaskDelete

app_name = 'todoapp2'
urlpatterns = [

    path('', homeView, name='home'),
    path('list/', todoListView, name='todoList'),
    path('create/', todoTaskCreate, name='todoTaskCreate'),
    path('<id>/delete/', todoTaskDelete, name='todoTaskDelete')
]