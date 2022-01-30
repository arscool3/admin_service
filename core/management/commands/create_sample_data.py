from datetime import date

from django.core.management.base import BaseCommand, CommandError

from core.models import Department, Client, LegalPerson


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        for i in range(1, 30001):
            Client.objects.create(id=int(f'{i}01'),
                                  first_name='Arslan',
                                  last_name='Yersain',
                                  patronymic='Askarovich',
                                  created_date=date.today(),
                                  email='arslsanersain@gmail.com',
                                  )
        for i in range(1, 201):
            LegalPerson.objects.create(id=int(f'{i}02'),
                                       created_date=date.today(),
                                       full_title='Agent',
                                       short_title='Agnt',
                                       inn='1' * 12,
                                       kpp='1' * 9)
        for i in range(1, 501):
            Department.objects.create(id=int(f'{i}03'),
                                      title='Department')