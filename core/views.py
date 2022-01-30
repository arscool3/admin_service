from rest_framework import generics

from core.models import Client, LegalPerson, Department
from core.serializers import ClientSerializer, LegalPersonSerializer, DepartmentSerializer


class GetClientView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class GetLegalPersonView(generics.ListAPIView):
    queryset = LegalPerson.objects.prefetch_related('departments__client')
    serializer_class = LegalPersonSerializer


class GetLegalPersonDetailView(generics.ListAPIView):
    queryset = LegalPerson.objects.all()
    serializer_class = LegalPersonSerializer


class GetDepartmentView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
