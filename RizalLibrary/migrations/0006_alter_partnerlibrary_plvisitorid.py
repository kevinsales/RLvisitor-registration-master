# Generated by Django 5.0.2 on 2024-02-21 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("RizalLibrary", "0005_alter_partnerlibrary_plvisitorid_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="partnerlibrary",
            name="plVisitorID",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
