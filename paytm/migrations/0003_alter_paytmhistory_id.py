# Generated by Django 4.0.2 on 2022-05-20 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paytm', '0002_auto_20200523_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paytmhistory',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
