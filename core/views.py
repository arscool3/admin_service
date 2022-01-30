from itertools import chain

from rest_framework import generics

from core.models import Client, LegalPerson, Department, VkSocialNetwork, FbSocialNetwork
from core.serializers import (
    ClientSerializer,
    LegalPersonSerializer,
    DepartmentSerializer,
    VkSocialNetworkSerializer,
    FbSocialNetworkSerializer,
)


class GetClientView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class GetVkAccountsView(generics.ListAPIView):
    def get_queryset(self):
        return VkSocialNetwork.objects.filter(client=self.kwargs['pk'])

    serializer_class = VkSocialNetworkSerializer


class GetFbAccountsView(generics.ListAPIView):
    def get_queryset(self):
        return FbSocialNetwork.objects.filter(client=self.kwargs['pk'])

    serializer_class = FbSocialNetworkSerializer


class GetLegalPersonView(generics.ListAPIView):
    queryset = LegalPerson.objects.prefetch_related('departments__client')
    serializer_class = LegalPersonSerializer


class GetDepartmentView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
