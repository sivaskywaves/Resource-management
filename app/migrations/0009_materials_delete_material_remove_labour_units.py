# Generated by Django 5.1.2 on 2024-12-11 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_labours_labour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('units', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Material',
        ),
        migrations.RemoveField(
            model_name='labour',
            name='units',
        ),
    ]
