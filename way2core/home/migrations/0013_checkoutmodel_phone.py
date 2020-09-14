# Generated by Django 3.0.1 on 2020-08-25 04:33

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_checkoutmodel_orderdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutmodel',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact Number', max_length=31),
        ),
    ]