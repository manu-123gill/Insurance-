# Generated by Django 4.0.2 on 2022-04-22 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0008_delete_registrationform'),
    ]

    operations = [
        migrations.CreateModel(
            name='registrationform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=30)),
            ],
        ),
    ]