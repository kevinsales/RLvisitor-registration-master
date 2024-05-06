# Generated by Django 5.0.2 on 2024-05-01 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("RizalLibrary", "0019_visitrequest_visitrequeststatus"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nonateneoaffiliated",
            name="naaInvitation",
            field=models.ImageField(upload_to="images/NAF/invitation/%Y%m%D"),
        ),
        migrations.AlterField(
            model_name="nonateneoaffiliated",
            name="naaPaymentConfirmation",
            field=models.ImageField(upload_to="images/NAF/payment/%Y%m%D"),
        ),
    ]