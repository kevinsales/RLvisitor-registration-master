# Generated by Django 4.1.7 on 2024-02-15 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RizalLibrary', '0003_alter_visitor_middlename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='visitorType',
            field=models.CharField(choices=[('PartnerLibrary', 'Partner Library'), ('NonAteneoAffiliated', 'Non Ateneo Affiliated'), ('AteneoAffiliated', 'Ateneo Affiliated')], default='AteneoAffiliated', max_length=50),
        ),
    ]