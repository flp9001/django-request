# Generated by Django 2.2 on 2019-12-22 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0006_alter_request_method_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='load_time',
            field=models.FloatField(null=True, verbose_name='load time'),
        ),
    ]
