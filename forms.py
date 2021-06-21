from django import forms

from app.models import Doctor
from app.models import Patient
from app.models import Appoinment


class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields="__all__"

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields="__all__"        

class AppoinmentForm(forms.ModelForm):
    class Meta:
        model=Appoinment
        fields="__all__"
