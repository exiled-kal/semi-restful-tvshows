# Generated by Django 2.2.11 on 2020-03-17 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='network',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='show',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
