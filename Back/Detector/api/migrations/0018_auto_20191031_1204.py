# Generated by Django 2.2.6 on 2019-10-31 12:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='input_image',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='return_images',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
