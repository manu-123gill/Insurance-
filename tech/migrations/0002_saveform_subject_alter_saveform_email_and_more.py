# Generated by Django 4.0.2 on 2022-04-12 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='saveform',
            name='subject',
            field=models.CharField(default='true', max_length=100),
        ),
        migrations.AlterField(
            model_name='saveform',
            name='email',
            field=models.EmailField(max_length=20),
        ),
        migrations.AlterField(
            model_name='saveform',
            name='message',
            field=models.CharField(max_length=100),
        ),
    ]