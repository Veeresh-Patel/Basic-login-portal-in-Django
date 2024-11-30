from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='photos/')
    document = models.FileField(upload_to='documents/')

from django.db import models

class FormSubmission(models.Model):
    HOSPITAL_CHOICES = [
        ('abc', 'ABC Hospital'),
        ('pqr', 'PQR Hospital'),
        ('xyz', 'XYZ Hospital'),
    ]
    TREATMENT_CHOICES = [
        ('conservative', 'Conservative'),
        ('surgical', 'Surgical'),
    ]

    name_of_hospital = models.CharField(max_length=3, choices=HOSPITAL_CHOICES)
    employee_id = models.CharField(max_length=50)
    name_of_employee = models.CharField(max_length=100)
    designation_of_employee = models.CharField(max_length=100)
    place_of_posting = models.CharField(max_length=100)
    name_of_patient = models.CharField(max_length=100)
    relationship_with_employee = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=15)
    email_id = models.EmailField()
    name_of_doctor = models.CharField(max_length=100)
    diagnosis = models.CharField(max_length=100)
    treatment_type = models.CharField(max_length=12, choices=TREATMENT_CHOICES)
    medical_advance_required = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    doctors_prescription = models.FileField(upload_to='prescriptions/')
    estimate = models.FileField(upload_to='estimates/')
