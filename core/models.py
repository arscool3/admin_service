from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from timezone_field import TimeZoneField

from .validators import validate_client_id, validate_legal_person_id,\
    validate_inn, validate_kpp, validate_department_id, validate_level


class SocialNetworkMixin(models.Model):
    link = models.URLField(max_length=128, unique=True, primary_key=True, blank=True)

    class Meta:
        abstract = True


class Client(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Активен'),
        ('Inactive', 'Не активен'),
    ]
    TYPE_CHOICES = [
        ('Primary', 'Первичный'),
        ('Repeated', 'Повторный'),
        ('External', 'Внешний'),
        ('Indirect', 'Косвенный'),
    ]
    SEX_CHOICES = [
        ('Male', 'Мужской'),
        ('Female', 'Женский'),
        ('Unknown', 'Неизвестно'),
    ]
    id = models.IntegerField(primary_key=True, validators=[validate_client_id], verbose_name='Идентификатор')
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=30, verbose_name='Отечество')
    created_date = models.DateField(verbose_name='Дата создания')
    modified_date = models.DateField(verbose_name='Дата изменения', blank=True, null=True)
    modified_status_date = models.DateField(verbose_name='Дата изменения статуса', blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, default='Active', max_length=10, verbose_name='Статус')
    type = models.CharField(choices=TYPE_CHOICES, default='Primary', max_length=10, verbose_name='Тип')
    email = models.EmailField(verbose_name='Почта')
    sex = models.CharField(choices=SEX_CHOICES, default='Unknown', max_length=10, verbose_name='Пол')
    timezone = TimeZoneField(default='Europe/Moscow', verbose_name='Часовой пояс')
    ok_link = models.URLField(max_length=128, blank=True, verbose_name='Одноклассники')
    instagram_link = models.URLField(max_length=128, blank=True, verbose_name='Instagram')
    telegram_link = models.URLField(max_length=128, blank=True, verbose_name='Telegram')
    whatsapp_link = models.URLField(max_length=128, blank=True, verbose_name='WhatsApp')
    viber_link = models.URLField(max_length=128, blank=True, verbose_name='Viber')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class LegalPerson(models.Model):
    id = models.IntegerField(primary_key=True, validators=[validate_legal_person_id], verbose_name='Идентификатор')
    create_date = models.DateField(verbose_name='Дата создания')
    modified_date = models.DateField(verbose_name='Дата изменения', blank=True, null=True)
    full_title = models.CharField(max_length=50, verbose_name='Полное название')
    short_title = models.CharField(max_length=10, verbose_name='Сокращенное название')
    inn = models.CharField(validators=[validate_inn], max_length=12, verbose_name='ИНН')
    kpp = models.CharField(validators=[validate_kpp], max_length=9, verbose_name='КПП')

    def __str__(self):
        return f'{self.short_title}'

    class Meta:
        verbose_name = 'Юридическое лицо'
        verbose_name_plural = 'Юридические лица'


class Department(models.Model):
    id = models.IntegerField(primary_key=True, validators=[validate_department_id], verbose_name='Идентификатор')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    level = models.IntegerField(validators=[validate_level], default=1)
    title = models.CharField(max_length=50, verbose_name='Название')
    client = models.ManyToManyField(Client, related_name='departments', verbose_name='Клиент')
    legal_person = models.ManyToManyField(LegalPerson, verbose_name='Юридическое лицо')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'


class VkSocialNetwork(SocialNetworkMixin):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')

    class Meta:
        verbose_name = 'Вконтакте'
        verbose_name_plural = 'Вконтакте'


class FbSocialNetwork(SocialNetworkMixin):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')

    class Meta:
        verbose_name = 'Facebook'
        verbose_name_plural = 'Facebook'


class Contact(models.Model):
    phone = PhoneNumberField(primary_key=True, unique=True, verbose_name='Телефон')
    is_main = models.BooleanField(default=True, verbose_name='Главный номер')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
