# Generated by Django 4.0 on 2022-01-05 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_form', '0002_alter_registered_users_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registered_users',
            options={'verbose_name': 'Registered User'},
        ),
        migrations.AddField(
            model_name='registered_users',
            name='contact',
            field=models.IntegerField(default=1234567890, max_length=10),
        ),
    ]