# Generated by Django 2.1 on 2018-08-10 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=500),
        ),
    ]
