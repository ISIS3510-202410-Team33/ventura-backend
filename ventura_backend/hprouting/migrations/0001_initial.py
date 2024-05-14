# Generated by Django 5.0.4 on 2024-05-12 06:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteAdjacency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distanceInM', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SiteType',
            fields=[
                ('type', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('img', models.ImageField(upload_to='sites')),
                ('neighbours', models.ManyToManyField(through='hprouting.SiteAdjacency', to='hprouting.site')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hprouting.sitetype')),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hprouting.university')),
            ],
        ),
    ]