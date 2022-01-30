from rest_framework import serializers

from core.models import Client, LegalPerson, Department


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ['timezone']


class DepartmentSerializer(serializers.ModelSerializer):
    client = ClientSerializer(many=True)

    class Meta:
        model = Department
        fields = '__all__'


class LegalPersonSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True)

    class Meta:
        model = LegalPerson
        fields = '__all__'
