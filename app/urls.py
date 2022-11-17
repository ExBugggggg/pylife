from unicodedata import category
from django.urls import path
from app.views.homeview import home
from app.views.todoview import todo
from app.views.userview import user
from app.views.billview import bill
from app.views.tagview import tag
from app.views.categoryview import category

urlpatterns = [
    path('', home.index, name='index'),
    path('todo', todo.index, name='todo'),
    # user module
    path('user/login', user.login, name='login'),
    path('user/logout', user.logout, name='logout'),
    path('user/failed', user.failed, name='failed'),
    # bill module
    path('bill/get', bill.get, name='get'),
    path('bill/add', bill.add, name='add'),
    path('bill/edit', bill.edit, name='edit'),
    # category module
    path('category/get', category.get, name='get'),
    path('category/add', category.add, name='add'),
    path('category/edit', category.edit, name='edit'),
    # tag module
    path('tag/add', tag.add, name='add'),
    path('tag/edit', tag.edit, name='edit'),
    path('tag/index', tag.index, name='index'),
]