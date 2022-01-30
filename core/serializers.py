from rest_framework import serializers

from core.models import Client, LegalPerson, Department, VkSocialNetwork, FbSocialNetwork


class VkSocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = VkSocialNetwork
        fields = '__all__'


class FbSocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FbSocialNetwork
        fields = '__all__'


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
