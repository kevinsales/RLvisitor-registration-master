# Generated by Django 5.0.2 on 2024-04-02 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("RizalLibrary", "0007_ateneoaffiliated_aainvitation_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ateneoaffiliated",
            name="aaInvitation",
        ),
        migrations.AlterField(
            model_name="ateneoaffiliated",
            name="aaIDPhoto",
            field=models.FileField(blank=True, upload_to=""),
        ),
    ]
