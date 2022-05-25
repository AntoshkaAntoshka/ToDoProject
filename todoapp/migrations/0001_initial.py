# Generated by Django 3.2.13 on 2022-05-23 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userworkapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=64, verbose_name='Title')),
                ('link_to_repo', models.TextField(blank=True, max_length=200, verbose_name='Link')),
                ('project_authors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userworkapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='TODO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=256, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapp.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='userworkapp.user')),
            ],
        ),
    ]