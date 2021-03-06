# Generated by Django 2.1.7 on 2019-05-13 09:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='balanceOwner',
            new_name='owner',
        ),
        migrations.AlterField(
            model_name='cashinorout',
            name='cash_in',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='cashinorout',
            name='cash_out',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='cashinorout',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='transition',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
