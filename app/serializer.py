from rest_framework import serializers
from app.models import Equations

class EquationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equations
        fields = '__all__'
