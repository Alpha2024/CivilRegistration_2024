# Generated by Django 4.2.6 on 2023-10-29 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crms', '0013_deathreg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deathreg',
            old_name='cause_ofdeath',
            new_name='cause_of_death',
        ),
    ]
