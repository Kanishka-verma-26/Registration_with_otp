# Generated by Django 4.0 on 2022-01-05 11:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_form', '0007_alter_registered_users_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_otp',
            name='expiration_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 5, 11, 42, 8, 946035)),
        ),
    ]
