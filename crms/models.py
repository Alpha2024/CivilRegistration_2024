from django.db import models
import random
import datetime
import string
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser



# Create your models here.
class User(AbstractUser):
    is_admin= models.BooleanField('Administrtor', default=False)
    is_employee= models.BooleanField('Registration Officer',default=False)
    

Gender =(
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Others')
)

District =(
    ('Kailauhun','Kailahun'),
    ('Kenema','Kenema'),
    ('Kono','Kono'),
    ('Bombali','Bombali'),
    ('Falaba','Falaba'),
    ('koinadugu','Koinadugu'),
    ('Tonkolili','Tokolili'),
    ('Kambia','Kambia'),
    ('Karene','Karene'),
    ('PortLoko','PortLoko'),
    ('Bo','Bo'),
    ('Bonth','Bonth'),
    ('Moyamba','Moyamba'),
    ('Pujehun','Pujehun'),
    ('Western Rural','Western Rural'),
    ('Western Urban','Wester Urban')
)

city =(
    ('Kailauhun','Kailahun'),
    ('Kenema','Kenema'),
    ('Freetown','Freetown'),
    ('Koidu Town','Koidu Town'),
    ('WaterLoo','WaterLoo'),
    ('Makeni','Makeni'),
    ('Magburaka','Magburaka'),
    ('Kambia','Kambia'),
    ('Kabala','Kabala'),
    ('Kamakwie','Kamakwie'),
    ('Bo','Bo'),
    ('Bonth','Bonth'),
    ('Moyamba','Moyamba'),
    ('Pujehun','Pujehun'),
    ('Bendugu','Bendugu'),
    ('Port Loko','Port Loko') 
)

Region =(
    ('Eastern','Eatern'),
    ('Northern','Northern'),
    ('North East','North East'),
    ('Southern','Southern'),
    ('Western','Western')
)

Religion=(
    ('Muslim','Muslim'),
    ('Christian','Christian')
)
MaritalStatus =(
    ('S','Single'),
    ('M','Married'),
    ('D','Divorce'),
    ('W','Widowed')
)

class Address(models.Model):
    address=models.CharField(max_length=50)
    region=models.CharField(max_length=50, choices=Region)
    city=models.CharField(max_length=50, choices=city)
    district=models.CharField(max_length=50, choices=District)


class Regcenter(models.Model):
    name=models.CharField(max_length=50)
    Address=models.OneToOneField(Address,on_delete=models.CASCADE)
    email=models.EmailField(null=True)


class Customer(models.Model):
    nin =models.CharField(max_length=7, unique=True, blank=True)
    first_name=models.CharField(max_length=50)
    middle_name=models.CharField(max_length=50, blank=True)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50, unique=True)
    gender =models.TextField(max_length=20, choices=Gender)
    dob=models.DateField(null=True)
    registered_date=models.DateField(null=True)
    fathername=models.CharField(max_length=50)
    mothername=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    district=models.CharField(max_length=20, choices=District)
    city=models.CharField(max_length=20, choices=city)
    region=models.CharField(max_length=20, choices=Region)
    religion=models.CharField(max_length=20, choices=Religion)
    contact=models.PositiveIntegerField(validators=[MinValueValidator(0)])
    height = models.DecimalField(max_digits=8, decimal_places=2)
    citizenship=models.CharField(max_length=50, default='SIERRA LEONEAN')
    photo=models.ImageField(upload_to='profile_pics/')
    

    def __str__(self):
        return self.first_name+" " +self.middle_name+" "+self.last_name
    
    def save(self, *args, **kwargs):

        if not self.nin:
            random_number = ''.join(random.choice(string.digits) for _ in range(5))
            self.nin = 'SL' + random_number
        super(Customer, self).save(*args, **kwargs)

class DeathReg(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    gender = models.TextField(max_length=20, choices=Gender)
    date_of_death = models.DateField()
    cause_of_death = models.CharField(max_length=100)
    time_of_death = models.TimeField()
    address= models.CharField(max_length=50)
    district= models.CharField(max_length=20, choices=District)
    city= models.CharField(max_length=20, choices=city)
    age = models.PositiveIntegerField()
    registered_date=models.DateField(null=True)
    photo=models.ImageField(upload_to='profile_pics/')

    def __str__(self):
        return self.first_name+" " +self.middle_name+" "+self.last_name
    




    

