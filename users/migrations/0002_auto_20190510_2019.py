# Generated by Django 2.0.6 on 2019-05-10 14:19

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='profile',
            name='utility',
            field=models.ImageField(upload_to=users.models.upload_pic_to, verbose_name='Utility Picture'),
        ),
    ]
