# Generated by Django 4.0.2 on 2022-04-21 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0005_dpt_empt'),
    ]

    operations = [
        migrations.CreateModel(
            name='showvideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=300)),
                ('video', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'showvideo',
            },
        ),
    ]