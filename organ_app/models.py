from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

BLOOD_GROUPS = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]

ORGANS_CHOICES = [
    ('Heart', 'Heart'),
    ('Liver', 'Liver'),
    ('Kidney', 'Kidney'),
    ('Lung', 'Lung'),
    ('Pancreas', 'Pancreas'),
    ('Intestine', 'Intestine'),
]
CAUSE_OF_DEATH_CHOICES = [
    ('Natural', 'Natural'),
    ('Accident', 'Accident'),
    ('Illness', 'Illness'),
    ('Other', 'Other'),
]
ORGANS_CHOICE = [
    ('Heart', 'Heart'),
    ('Liver', 'Liver'),
    ('Kidney', 'Kidney'),
    ('Lung', 'Lung'),
    ('Pancreas', 'Pancreas'),
    ('Intestine', 'Intestine'),
]

class User(AbstractUser):
    is_donor = models.BooleanField(default=False, verbose_name="Is Donor")
    is_patient = models.BooleanField(default=False, verbose_name="Is Patient")
    name = models.CharField(max_length=100,null=True, blank=True)
    mobile = models.CharField(max_length=15,null=True, blank=True)
    address = models.CharField(max_length=200,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    country = models.CharField(max_length=100,null=True, blank=True)
    district = models.CharField(max_length=100,null=True, blank=True)
    gender = models.CharField(max_length=10,null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    blood_grou = models.CharField(max_length=3, choices=BLOOD_GROUPS, null=True, blank=True)  # Set a default value
    organs_to_donat = models.CharField(max_length=20, choices=ORGANS_CHOICES, null=True, blank=True)
    status = models.BooleanField(default=False)
    cause_of_death = models.CharField(max_length=20, choices=CAUSE_OF_DEATH_CHOICES, null=True, blank=True)
    needed_organ = models.CharField(max_length=20, choices=ORGANS_CHOICE, null=True, blank=True)


    def __str__(self):
        return self.username
    
class OrganRequest(models.Model):
    donor_id= models.IntegerField(null=True, blank=True)
    patient_id= models.IntegerField(null=True, blank=True)
    donor_name = models.CharField(max_length=100,null=True, blank=True)
    donor_age = models.PositiveIntegerField(null=True, blank=True)
    donor_email= models.EmailField(null=True, blank=True)
    status = models.BooleanField(default=False)
    needed_organ= models.CharField(max_length=20,null=True, blank=True)
    patient_name = models.CharField(max_length=100,null=True, blank=True)
    patient_age = models.PositiveIntegerField(null=True, blank=True)
    patient_email= models.EmailField(null=True, blank=True)
    def __str__(self):
        return self.donor_name