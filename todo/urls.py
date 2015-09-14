# -*- coding: utf-8 -*-
__author__ = 'akiokio'

from django.conf.urls import url

from todo.views import TodoList

urlpatterns = [
    url(r'^$', TodoList.as_view(), name="todo_list")
]