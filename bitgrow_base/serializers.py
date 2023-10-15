from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class KOLSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.KOL
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # data.pop('task', None)
        # data.update(TaskSerializer(instance.task).data)
        data['task'] = TaskSerializer(instance.task).data
        data['kol'] = KOLSerializer(instance.kol).data

        return data


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = '__all__'
