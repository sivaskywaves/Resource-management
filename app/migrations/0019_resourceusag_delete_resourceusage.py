# Generated by Django 5.1.2 on 2024-12-14 06:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_resourceusage_equipment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceUsag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usage_date', models.DateField()),
                ('usage_quantity', models.IntegerField(blank=True, null=True)),
                ('resource_type', models.CharField(max_length=255)),
                ('equipment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.equipment')),
                ('labour', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.labour')),
                ('material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.material')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.project')),
            ],
        ),
        migrations.DeleteModel(
            name='ResourceUsage',
        ),
    ]
