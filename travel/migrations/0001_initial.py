# Generated by Django 5.1.4 on 2024-12-11 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tvl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('popular_season', models.CharField(max_length=100)),
            ],
        ),
    ]
