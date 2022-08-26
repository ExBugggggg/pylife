from django.urls import path
from app.views.homeview import home
from app.views.todoview import todo
from app.views.userview import user
from app.views.billview import bill

urlpatterns = [
    path('', home.index, name='index'),
    path('todo', todo.index, name='todo'),
    # user module
    path('user/login', user.login, name='login'),
    path('user/logout', user.logout, name='logout'),
    # bill module
    path('bill/get', bill.get, name="get"),
    path('bill/add', bill.add, name="add"),
    path('bill/edit', bill.edit, name='edit')
]