# Generated by Django 3.0.4 on 2021-01-15 14:29

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0006_auto_20201230_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='steps',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True),
        ),
    ]