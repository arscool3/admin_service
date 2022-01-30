from django.urls import path

from core.views import GetClientView, GetDepartmentView, GetLegalPersonView, GetLegalPersonDetailView

urlpatterns = [
    path('clients/', GetClientView.as_view()),
    path('legal_persons/', GetLegalPersonView.as_view()),
    path('departments/', GetDepartmentView.as_view()),
]
