# Generated by Django 4.0.1 on 2022-01-30 08:27

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_legalperson_alter_client_sex_alter_client_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legalperson',
            name='inn',
            field=models.IntegerField(validators=[core.validators.validate_inn]),
        ),
        migrations.AlterField(
            model_name='legalperson',
            name='kpp',
            field=models.IntegerField(validators=[core.validators.validate_kpp]),
        ),
    ]