# Generated by Django 4.2.3 on 2023-07-24 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tmglobal', '0006_remove_noc_users_departmento_noc_users_noc_cargo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Noc_Users',
        ),
    ]