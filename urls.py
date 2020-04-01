from django.urls import path,include
from . import views
urlpatterns = [
        path('',views.index, name='index'),
        path('add',views.newTodo,name='new'),
        path('complete/<todo_id>',views.completeTodo,name='complete'),
        path('delete',views.deleteTodo,name='delete'),


    ]
