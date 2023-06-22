# Generated by Django 4.1.4 on 2023-06-16 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="societytype",
            name="typeCode",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="application",
            name="disposalDate",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="application",
            name="receivedDate",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="application",
            name="societyType",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="main.societytype",
            ),
        ),
        migrations.AlterField(
            model_name="district",
            name="districtCode",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.CreateModel(
            name="Society",
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
                ("Address", models.CharField(blank=True, max_length=1000, null=True)),
                ("Date", models.DateField(blank=True, null=True)),
                (
                    "district",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.district"
                    ),
                ),
                (
                    "societyType",
                    models.ForeignKey(
                        blank=True,
                        null=True,
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