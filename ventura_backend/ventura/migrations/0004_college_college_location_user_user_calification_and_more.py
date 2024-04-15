# Generated by Django 5.0.4 on 2024-04-15 01:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ventura", "0003_remove_users_college_id_delete_colleges"),
    ]

    operations = [
        migrations.CreateModel(
            name="College",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="College_location",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("floors", models.IntegerField()),
                ("restaurants", models.IntegerField()),
                ("green_zones", models.IntegerField()),
                ("obstructions", models.BooleanField()),
                (
                    "college",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ventura.college",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                (
                    "college",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ventura.college",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User_calification",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("calification", models.IntegerField()),
                ("description", models.TextField(max_length=300)),
                ("date", models.DateField(auto_now=True)),
                (
                    "college_location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ventura.college_location",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ventura.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User_frequency",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("frequency", models.IntegerField()),
                (
                    "college_location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ventura.college_location",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ventura.user"
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Users",
        ),
    ]
