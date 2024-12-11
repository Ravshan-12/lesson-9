# Generated by Django 5.1.4 on 2024-12-11 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('sport_type', models.CharField(max_length=100)),
            ],
        ),
    ]
