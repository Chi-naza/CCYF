# Generated by Django 4.1.3 on 2022-12-09 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Divine', '0003_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(upload_to='membersImage'),
        ),
    ]
