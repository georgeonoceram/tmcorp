# Generated by Django 4.2.3 on 2023-07-20 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('tmglobal', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NocUsers',
            new_name='Noc_Users',
        ),
        migrations.RenameField(
            model_name='noc_users',
            old_name='noccargo',
            new_name='noc_cargo',
        ),
    ]