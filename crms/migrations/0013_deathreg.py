# Generated by Django 4.2.6 on 2023-10-28 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crms', '0012_alter_customer_citizenship'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeathReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.TextField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Others')], max_length=20)),
                ('date_of_death', models.DateField()),
                ('cause_ofdeath', models.CharField(max_length=100)),
                ('time_of_death', models.TimeField()),
                ('address', models.CharField(max_length=50)),
                ('district', models.CharField(choices=[('Kailauhun', 'Kailahun'), ('Kenema', 'Kenema'), ('Kono', 'Kono'), ('Bombali', 'Bombali'), ('Falaba', 'Falaba'), ('koinadugu', 'Koinadugu'), ('Tonkolili', 'Tokolili'), ('Kambia', 'Kambia'), ('Karene', 'Karene'), ('PortLoko', 'PortLoko'), ('Bo', 'Bo'), ('Bonth', 'Bonth'), ('Moyamba', 'Moyamba'), ('Pujehun', 'Pujehun'), ('Western Rural', 'Western Rural'), ('Western Urban', 'Wester Urban')], max_length=20)),
                ('city', models.CharField(choices=[('Kailauhun', 'Kailahun'), ('Kenema', 'Kenema'), ('Freetown', 'Freetown'), ('Koidu Town', 'Koidu Town'), ('WaterLoo', 'WaterLoo'), ('Makeni', 'Makeni'), ('Magburaka', 'Magburaka'), ('Kambia', 'Kambia'), ('Kabala', 'Kabala'), ('Kamakwie', 'Kamakwie'), ('Bo', 'Bo'), ('Bonth', 'Bonth'), ('Moyamba', 'Moyamba'), ('Pujehun', 'Pujehun'), ('Bendugu', 'Bendugu'), ('Port Loko', 'Port Loko')], max_length=20)),
                ('age', models.PositiveIntegerField()),
                ('registereddate', models.DateField(null=True)),
            ],
        ),
    ]
