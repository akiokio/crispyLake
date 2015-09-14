# -*- coding: utf-8 -*-
__author__ = 'akiokio'

from rest_framework import serializers

from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo