# Generated by Django 4.0.4 on 2022-06-06 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=50)),
                ('course_name', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
    ]
