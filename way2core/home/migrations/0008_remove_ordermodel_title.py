# Generated by Django 3.0.1 on 2020-08-24 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_ordermodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='title',
        ),
    ]
