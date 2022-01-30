# Generated by Django 4.0.1 on 2022-01-30 09:27

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_client_options_alter_department_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='is_main',
            field=models.BooleanField(default=True, verbose_name='Главный номер'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, primary_key=True, region=None, serialize=False, unique=True, verbose_name='Телефон'),
        ),
    ]
