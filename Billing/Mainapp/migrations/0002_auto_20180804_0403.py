# Generated by Django 2.0.7 on 2018-08-04 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billdetails',
            name='Rs1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='billdetails',
            name='Rs10',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='billdetails',
            name='Rs100',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='billdetails',
            name='Rs2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='billdetails',
            name='Rs20',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='billdetails',
            name='Rs2000',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='billdetails',
            name='Rs5',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='billdetails',
            name='Rs50',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='billdetails',
            name='Rs500',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='billdetails',
            name='bill',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='billdetails',
            name='change',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='billdetails',
            name='paid',
            field=models.IntegerField(default=0),
        ),
    ]