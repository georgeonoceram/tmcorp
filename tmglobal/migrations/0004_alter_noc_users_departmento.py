# Generated by Django 4.2.3 on 2023-07-20 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmglobal', '0003_remove_noc_users_noc_cargo_noc_users_departmento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noc_users',
            name='departmento',
            field=models.CharField(max_length=50),
        ),
    ]
