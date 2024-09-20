# Generated by Django 5.1.1 on 2024-09-20 16:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('opening', models.DateTimeField()),
                ('closing', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('year_of_study', models.DateField()),
                ('major', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UniversityStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('status', models.CharField(max_length=20)),
                ('facility', models.ManyToManyField(to='panner.facility')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panner.universitystaff')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='panner.event')),
                ('facility', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='panner.facility')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panner.student')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('checkin_time', models.DateTimeField()),
                ('checkout_time', models.DateTimeField()),
                ('booking_status', models.CharField(max_length=20)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panner.facility')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panner.student')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=20)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panner.student')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panner.universitystaff')),
            ],
        ),
        migrations.AddField(
            model_name='facility',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panner.universitystaff'),
        ),
    ]
