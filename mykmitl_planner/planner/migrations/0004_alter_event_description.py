# Generated by Django 5.1.1 on 2024-09-30 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0003_facility_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
