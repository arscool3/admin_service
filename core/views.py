from rest_framework import generics

from core.models import Client, LegalPerson, Department
from core.serializers import ClientSerializer, LegalPersonSerializer, DepartmentSerializer


class GetClientView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class GetLegalPersonView(generics.ListAPIView):
    queryset = LegalPerson.objects.all()
    # def get_queryset(self):
    #     departaments = Department.objects.all()
    #     legal_persons = LegalPerson.objects.all()
    #     for legal_person in legal_persons:
    #         for departament in departaments:
    #             cur_legal_persons = LegalPerson.objects.filter(departament__in=[departament.id])
    #             if legal_person in cur_legal_persons:
    #
    serializer_class = LegalPersonSerializer


class GetLegalPersonDetailView(generics.ListAPIView):
    queryset = LegalPerson.objects.all()
    serializer_class = LegalPersonSerializer


class GetDepartmentView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
