# Generated by Django 4.0.2 on 2022-04-21 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0006_showvideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='registrationform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Password', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
    ]