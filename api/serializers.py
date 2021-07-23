from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'description',
            'complete',
        )
        model = Task

    def validate_description(self, value):
        if value is None:
            raise serializers.ValidationError('La descripción es obligatoria')
        return value
