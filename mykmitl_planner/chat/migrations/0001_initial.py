# Generated by Django 5.1.1 on 2024-09-23 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planner', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=20)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.universitystaff')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.student')),
            ],
        ),
    ]
