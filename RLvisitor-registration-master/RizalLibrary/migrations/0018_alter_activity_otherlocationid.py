# Generated by Django 5.0.2 on 2024-05-01 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "RizalLibrary",
            "0017_alter_activity_endpage_alter_activity_startpage_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="activity",
            name="otherLocationID",
            field=models.CharField(max_length=4),
        ),
    ]
