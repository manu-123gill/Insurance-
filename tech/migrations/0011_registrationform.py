# Generated by Django 4.0.2 on 2022-04-26 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0010_delete_registrationform'),
    ]

    operations = [
        migrations.CreateModel(
            name='registrationform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=30)),
                ('pin', models.IntegerField()),
                ('adhar_no', models.IntegerField()),
            ],
            options={
                'db_table': 'registrationform',
            },
        ),
    ]
