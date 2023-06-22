# Generated by Django 4.1.4 on 2023-06-16 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SocietyType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("societyType", models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="State",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stateName", models.CharField(max_length=500)),
                ("stateCode", models.CharField(max_length=50)),
                ("isUt", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="District",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("districtName", models.CharField(max_length=500)),
                ("districtCode", models.CharField(max_length=50)),
                (
                    "state",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.state"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Application",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("societyName", models.CharField(max_length=500)),
                ("receivedDate", models.DateField()),
                ("disposalDate", models.DateField()),
                (
                    "district",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.district"
                    ),
                ),
                (
                    "societyType",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.societytype",
                    ),
                ),
                (
                    "state",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.state"
                    ),
                ),
            ],
        ),
    ]
