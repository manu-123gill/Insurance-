# Generated by Django 4.0.2 on 2022-04-13 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0002_saveform_subject_alter_saveform_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('des', models.TextField()),
                ('image', models.ImageField(upload_to='pictures')),
            ],
            options={
                'db_table': 'blogs',
            },
        ),
    ]