# psicomedic/views.py

from django.shortcuts import render, get_object_or_404
from .models import Psychologist, Patient, Appointment

def list_psychologist(request):
    psychologists = Psychologist.objects.all()
    return render(request, 'psicomedic/list_psychologist.html', {'psychologists': psychologists})

def get_psychologist(request, pk):
    psychologist = get_object_or_404(Psychologist, pk=pk)
    return render(request, 'psicomedic/get_psychologist.html', {'psychologist': psychologist})

def list_patients(request):
    patients = Patient.objects.all()
    return render(request, 'psicomedic/list_patients.html', {'patients': patients})

def get_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'psicomedic/get_patient.html', {'patient': patient})

def list_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'psicomedic/list_appointments.html', {'appointments': appointments})

def get_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'psicomedic/get_appointment.html', {'appointment': appointment})
