# Generated by Django 4.2.11 on 2024-04-22 13:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Conference",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "conferences",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Division",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "divisions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.IntegerField(blank=True, primary_key=True, serialize=False),
                ),
                ("name", models.TextField(blank=True, null=True)),
                ("grade", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "players",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.TextField(blank=True, null=True)),
                ("g", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "teams",
                "managed": False,
            },
        ),
        migrations.DeleteModel(
            name="Conferences",
        ),
        migrations.DeleteModel(
            name="Divisions",
        ),
        migrations.DeleteModel(
            name="Players",
        ),
        migrations.DeleteModel(
            name="Teams",
        ),
    ]
