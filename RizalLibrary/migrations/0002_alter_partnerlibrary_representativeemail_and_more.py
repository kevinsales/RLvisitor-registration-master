# Generated by Django 4.1.7 on 2024-02-14 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RizalLibrary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnerlibrary',
            name='representativeEmail',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='partnerlibrary',
            name='representativeID',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='partnerlibrary',
            name='representativeName',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
