# Generated by Django 4.2.6 on 2023-10-31 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crms', '0015_deathreg_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='deathreg',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]