# Generated by Django 4.2.6 on 2023-10-23 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crms', '0005_rename_first_name_customer_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='religion',
            field=models.CharField(choices=[('Muslim', 'Muslim'), ('Christian', 'Christian')], default='', max_length=20),
            preserve_default=False,
        ),
    ]