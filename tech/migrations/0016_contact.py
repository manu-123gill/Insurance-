# Generated by Django 4.0.2 on 2022-05-20 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0015_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=30)),
                ('Subject', models.CharField(max_length=30)),
                ('Message', models.CharField(max_length=30)),
            ],
        ),
    ]
