# Generated by Django 5.0.2 on 2024-05-02 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("RizalLibrary", "0021_alter_nonateneoaffiliated_naainvitation_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ateneoaffiliated",
            name="aaCourse",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="ateneoaffiliated",
            name="aaIDPhoto",
            field=models.ImageField(upload_to="images/AF/id"),
        ),
        migrations.AlterField(
            model_name="ateneoaffiliated",
            name="aaLastSem",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="ateneoaffiliated",
            name="aaPaymentConfirmation",
            field=models.ImageField(upload_to="images/AF/payment"),
        ),
        migrations.AlterField(
            model_name="ateneoaffiliated",
            name="aaYear",
            field=models.IntegerField(null=True),
        ),
    ]
