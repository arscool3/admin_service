from django.contrib import admin
from .models import Client, Contact, FbSocialNetwork, VkSocialNetwork, LegalPerson, Department


class ContactInline(admin.TabularInline):
    model = Contact


class FbSocialNetworkInline(admin.TabularInline):
    model = FbSocialNetwork


class VkSocialNetworkInline(admin.TabularInline):
    model = VkSocialNetwork


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    inlines = [ContactInline, FbSocialNetworkInline, VkSocialNetworkInline]


admin.site.register(LegalPerson)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_department',)

    @admin.display(description='Количество клиентов')
    def display_department(self, obj):
        return len(Client.objects.filter(departments__in=[obj.id]))
