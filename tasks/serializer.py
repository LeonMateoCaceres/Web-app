from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__' #Trae todos los campos de la tabla
        #fields = ('id', 'title', 'description', 'done') traer los campos de la tabla uno por uno
    