from django.urls import path
from app.views.homeview import home
from app.views.todoview import todo
from app.views.userview import user

urlpatterns = [
    path('', home.index, name='index'),
    path('todo', todo.index, name='todo'),
    # user module
    path('user/login', user.login, name='login'),
    path('user/logout', user.logout, name='logout'),
]