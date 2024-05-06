# Generated by Django 5.0.2 on 2024-05-06 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RizalLibrary', '0030_remove_locationvisitrequest_locationid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterEvent',
            fields=[
                ('eventID', models.AutoField(primary_key=True, serialize=False)),
                ('eventName', models.CharField(max_length=100)),
                ('locationID', models.SmallIntegerField()),
                ('eventDate', models.DateField()),
                ('participantsList', models.FileField(upload_to='files/event')),
            ],
        ),
        migrations.AlterField(
            model_name='accountmoreinfo',
            name='accountType',
            field=models.CharField(choices=[('Librarian', 'Librarian'), ('Admin', 'Admin')], max_length=10),
        ),
    ]
