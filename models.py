# psicomedic/models.py

from django.db import models

class Psychologist(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthdate = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthdate = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    biography = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Appointment(models.Model):
    appointment_date = models.DateField()
    title = models.CharField(max_length=255)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
