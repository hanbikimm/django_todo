from django.contrib import admin
from django.urls import path
from todo.views import *

app_name='todo'
urlpatterns = [
    path('', TodoList.as_view(), name='index'),
    path('<int:pk>/', TodoDetail.as_view(), name='detail'),
    path('enter/', TodoEnter.as_view(), name='enter'),
    path('update/<int:pk>', TodoUpdate.as_view(), name='update'),
    path('delete/<int:pk>', TodoDelete.as_view(), name='delete'),

]