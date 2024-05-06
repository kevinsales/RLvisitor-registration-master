# Generated by Django 5.0.2 on 2024-02-19 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("RizalLibrary", "0004_alter_visitor_visitortype"),
    ]

    operations = [
        migrations.AlterField(
            model_name="partnerlibrary",
            name="plVisitorID",
            field=models.IntegerField(
                default=0, max_length=50, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="visitor",
            name="idNumber",
            field=models.CharField(max_length=50),
        ),
    ]