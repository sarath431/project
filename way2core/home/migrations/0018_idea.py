# Generated by Django 3.0.1 on 2020-09-03 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_iotlistmodel_diagram'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phno', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('diagram', models.ImageField(blank=True, default='default.png', null=True, upload_to='')),
            ],
        ),
    ]
