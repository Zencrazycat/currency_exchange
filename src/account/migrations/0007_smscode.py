# Generated by Django 2.2.10 on 2020-03-30 09:01

import account.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_user_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmsCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('code', models.PositiveSmallIntegerField(default=account.models.generate_sms_code)),
                ('is_activated', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sms_codes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
