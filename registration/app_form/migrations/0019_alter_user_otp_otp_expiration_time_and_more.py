# Generated by Django 4.0 on 2022-01-10 08:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_form', '0018_alter_user_otp_otp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_otp',
            name='otp_expiration_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 10, 8, 10, 34, 915018, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user_otp',
            name='otp_generate_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 10, 8, 8, 34, 914977, tzinfo=utc)),
        ),
    ]
