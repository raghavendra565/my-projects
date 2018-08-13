# Generated by Django 2.1 on 2018-08-10 10:44

import MainApp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=MainApp.models.file1)),
                ('status', models.BooleanField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoriecarousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=MainApp.models.file3)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to=MainApp.models.file2)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Listing_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=MainApp.models.file5)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.TextField(max_length=80)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, default='', max_length=254, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=MainApp.models.file4)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categorie', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='MainApp.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='MainpageCarousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, default='', max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=80)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='MainApp.Roles')),
            ],
        ),
        migrations.AddField(
            model_name='mainpagecarousel',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='MainApp.Users'),
        ),
        migrations.AddField(
            model_name='listings',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='MainApp.Users'),
        ),
        migrations.AddField(
            model_name='listing_images',
            name='listing',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='MainApp.Listings'),
        ),
        migrations.AddField(
            model_name='listing_images',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='MainApp.Users'),
        ),
        migrations.AddField(
            model_name='categories',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='MainApp.Users'),
        ),
        migrations.AddField(
            model_name='categoriecarousel',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='MainApp.Categories'),
        ),
        migrations.AddField(
            model_name='categoriecarousel',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='MainApp.Users'),
        ),
        migrations.AddField(
            model_name='carousel',
            name='mainpage',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='MainApp.MainpageCarousel'),
        ),
        migrations.AddField(
            model_name='carousel',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='MainApp.Users'),
        ),
    ]