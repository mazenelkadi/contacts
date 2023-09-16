from django.db import models
import os
from django.contrib.auth.models import User

class UserContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    prefix = models.CharField(max_length=30, null=True, blank=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    sur_name = models.CharField(max_length=30, null=True, blank=True)
    suffix = models.CharField(max_length=30, null=True, blank=True)

    company_name = models.CharField(max_length=40, null=True, blank=True)
    
    phone_choices = (
        ('Mobile', 'Mobile'),
        ('Work', 'Work'),
        ('Home', 'Home'),
        ('Office', 'Office')
    )

    common_choices = (
        ('Work', 'Work'),
        ('Home', 'Home'),
        ('Personal', 'Personal')
    )
    
    phonenumber = models.CharField(max_length=15, null=True, blank=True)
    phone_type = models.CharField(max_length=15, choices=phone_choices, default='M', null=True, blank=True)
    
    email = models.CharField(max_length=50, null=True, blank=True)
    email_type = models.CharField(max_length=10, choices=common_choices, default='W', blank=True)
    
    address = models.TextField(max_length=150, null=True, blank=True)
    address_type= models.CharField(max_length = 10, choices = common_choices, default = 'W', blank = True)
   
    date_choices = (
        ('Birthday', 'Birthday'),
        ('Anniversary', 'Anniversary')
    )
    
    occasion_date = models.DateField(null=True, blank=True)  
    occasion = models.CharField(max_length=15, choices=date_choices, null=True, blank=True)
    
    relations = (
        ('Assistant', 'Assistant'),
        ('Brother', 'Brother'),
        ('Son', 'Son'),
        ('Daughter', 'Daughter'),
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Friend', 'Friend'),
        ('Manager', 'Manager'),
        ('Partner', 'Partner'),
        ('Sister', 'Sister'),
        ('Spouse', 'Spouse'),
        ('Relative', 'Relative')
    )
    relation = models.CharField(max_length=15, choices=relations, blank=True)
    
    description = models.TextField(max_length=200, null=True, blank=True)