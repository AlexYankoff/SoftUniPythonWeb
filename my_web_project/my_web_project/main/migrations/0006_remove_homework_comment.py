# Generated by Django 3.2.5 on 2021-07-06 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210706_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='comment',
        ),
    ]