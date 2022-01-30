from django.urls import path

from core.views import GetClientView, GetDepartmentView, GetLegalPersonView, GetVkAccountsView, GetFbAccountsView

urlpatterns = [
    path('clients/', GetClientView.as_view()),
    path('vk/clients/<int:pk>', GetVkAccountsView.as_view()),
    path('fb/clients/<int:pk>', GetFbAccountsView.as_view()),
    path('legal_persons/', GetLegalPersonView.as_view()),
    path('departments/', GetDepartmentView.as_view()),
]
