from django import forms
from .models import *

class EmployeeDetailsForm(forms.ModelForm):
    class Meta:
        model= EmployeeDetails
        fields='__all__'


class UpdateEmployeeDetailsForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetails
        fields = '__all__'


class MonthForm(forms.ModelForm):
    class Meta:
        model = PayslipMonth
        fields = '__all__'


class SalaryDetailForm(forms.ModelForm):
    class Meta:
        model = SalaryDetail
        fields = '__all__'
        

class UpdateSalaryDetailForm(forms.ModelForm):
    class Meta:
        model = SalaryDetail
        fields = '__all__'
