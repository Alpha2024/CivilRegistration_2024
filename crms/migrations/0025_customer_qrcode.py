# Generated by Django 4.2.6 on 2023-11-20 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crms', '0024_rename_registereddate_deathreg_registered_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='qrcode',
            field=models.ImageField(blank=True, upload_to='qr_codes'),
        ),
    ]
