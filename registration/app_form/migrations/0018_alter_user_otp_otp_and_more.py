# Generated by Django 4.0 on 2022-01-07 09:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_form', '0017_remove_user_otp_current_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_otp',
            name='otp',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='user_otp',
            name='otp_expiration_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 7, 9, 48, 49, 876776, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user_otp',
            name='otp_generate_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 7, 9, 43, 49, 876734, tzinfo=utc)),
        ),
    ]