# Generated by Django 3.2.13 on 2022-05-25 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userworkapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=100, unique=True, verbose_name='E-mail'),
        ),
    ]