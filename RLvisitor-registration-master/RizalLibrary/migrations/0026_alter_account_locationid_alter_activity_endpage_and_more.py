# Generated by Django 5.0.2 on 2024-05-05 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("RizalLibrary", "0025_alter_activity_requestpurpose"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="locationID",
            field=models.SmallIntegerField(max_length=2),
        ),
        migrations.AlterField(
            model_name="activity",
            name="endPage",
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name="activity",
            name="locationID",
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name="activity",
            name="startPage",
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name="activity",
            name="visitorRequestID",
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name="ateneoaffiliated",
            name="aaType",
            field=models.CharField(
                choices=[
                    ("ALUMNI (Admu)", "ALUMNI (Admu)"),
                    ("Basic Education Unit (BEU)", "Basic Education Unit (BEU)"),
                    ("Leave of Absence (LOA)", "Leave of Absence (LOA)"),
                ],
                default="ALUMNI (Admu)",
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name="ateneoaffiliated",
            name="aaVisitorID",
            field=models.SmallIntegerField(
                max_length=5, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="ateneoaffiliated",
            name="aaYear",
            field=models.IntegerField(max_length=4),
        ),
        migrations.AlterField(
            model_name="event",
            name="participantsNum",
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name="location",
            name="locationID",
            field=models.AutoField(max_length=2, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="nonateneoaffiliated",
            name="naaType",
            field=models.CharField(
                choices=[
                    ("Public Researcher", "Public Researcher"),
                    ("Library Guest ", "Library Guest"),
                    ("Vendor/Supplier", "Vendor/Supplier"),
                ],
                default="Library Guest ",
                max_length=29,
            ),
        ),
        migrations.AlterField(
            model_name="nonateneoaffiliated",
            name="naaVisitorID",
            field=models.SmallIntegerField(
                max_length=5, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="partnerlibrary",
            name="plVisitorID",
            field=models.SmallIntegerField(
                max_length=5, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="visitor",
            name="visitorID",
            field=models.AutoField(max_length=5, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="visitor",
            name="visitorType",
            field=models.CharField(
                choices=[
                    ("PartnerLibrary", "Partner Library"),
                    ("NonAteneoAffiliated", "Non Ateneo Affiliated"),
                    ("AteneoAffiliated", "Ateneo Affiliated"),
                ],
                default="AteneoAffiliated",
                max_length=22,
            ),
        ),
        migrations.AlterField(
            model_name="visitrequest",
            name="visitRequestStatus",
            field=models.SmallIntegerField(default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name="visitrequestday",
            name="visitRequestDayID",
            field=models.AutoField(max_length=5, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="visitrequestday",
            name="visitRequestID",
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name="visitrequestday",
            name="visitStatus",
            field=models.SmallIntegerField(default=0),
        ),
    ]