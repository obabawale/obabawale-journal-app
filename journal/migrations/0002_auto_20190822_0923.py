# Generated by Django 2.2.2 on 2019-08-22 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='title',
            field=models.CharField(max_length=64),
        ),
    ]
