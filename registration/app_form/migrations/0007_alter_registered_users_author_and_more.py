# Generated by Django 4.0 on 2022-01-05 11:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app_form', '0006_remove_registered_users_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registered_users',
            name='author',
            field=models.ForeignKey(default='', editable=False, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AlterField(
            model_name='user_otp',
            name='expiration_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 5, 11, 41, 43, 744483)),
        ),
    ]
