# Generated by Django 2.2.10 on 2020-03-22 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_activationcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activationcode',
            name='timeout',
        ),
    ]
