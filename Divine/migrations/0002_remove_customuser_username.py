# Generated by Django 4.1.3 on 2022-12-09 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Divine', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]
