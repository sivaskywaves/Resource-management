# Generated by Django 5.1.2 on 2024-12-04 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_equipments_delete_equipment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Equipments',
            new_name='Equipment',
        ),
    ]
