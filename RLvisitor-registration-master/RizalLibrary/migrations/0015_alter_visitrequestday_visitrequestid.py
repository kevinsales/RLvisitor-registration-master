# Generated by Django 5.0.2 on 2024-05-01 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("RizalLibrary", "0014_rename_visitorid_visitrequest_visitorid_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="visitrequestday",
            name="visitRequestID",
            field=models.IntegerField(),
        ),
    ]