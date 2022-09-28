from todolist.views import register, show_todolist #sesuaikan dengan nama fungsi yang dibuat
from django.urls import path
from todolist.views import *
app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'), 
    path('create-task/', create_task, name='create-task'), 
    path('delete-task/<int:pk>/', delete_task, name='delete-task'),
    path('change-status/<int:pk>/', change_status, name='change-status'),
]