from rest_framework import serializers

from core.models import Client, LegalPerson, Department


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ['timezone']


class LegalPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalPerson
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
