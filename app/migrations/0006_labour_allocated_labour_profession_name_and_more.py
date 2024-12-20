# Generated by Django 5.1.2 on 2024-12-11 06:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_equipment_ids_project_equipment_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='labour',
            name='allocated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='labour',
            name='profession_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='labour',
            name='profession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profession'),
        ),
    ]
