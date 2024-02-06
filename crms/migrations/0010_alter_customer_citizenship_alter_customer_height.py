# Generated by Django 4.2.6 on 2023-10-25 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crms', '0009_remove_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='citizenship',
            field=models.CharField(default='SIERRA LEONEAN', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='height',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=1),
        ),
    ]