# Generated by Django 3.2.13 on 2022-05-16 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=64, verbose_name='Username')),
                ('first_name', models.CharField(max_length=64, verbose_name='Firstname')),
                ('last_name', models.CharField(max_length=64, verbose_name='Lastname')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='E-mail')),
            ],
        ),
    ]