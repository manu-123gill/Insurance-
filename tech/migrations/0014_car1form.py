# Generated by Django 4.0.2 on 2022-05-06 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0013_businessform'),
    ]

    operations = [
        migrations.CreateModel(
            name='car1form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company', models.CharField(max_length=30)),
                ('Model', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('registrationdate', models.CharField(max_length=30)),
                ('number', models.CharField(max_length=30)),
            ],
        ),
    ]
