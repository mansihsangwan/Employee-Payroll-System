from django.db import models
from django.conf import settings
from django.urls import reverse
from datetime import datetime

class EmployeeDetails(models.Model):
    first_name      = models.CharField(max_length=100)
    last_name       = models.CharField(max_length=100)
    photo           = models.ImageField(upload_to='Photos/')
    email           = models.EmailField(max_length=30)
    mobile          = models.CharField(max_length=13)
    designation     = models.CharField(max_length=50)
    employee_id     = models.IntegerField()
    date_of_joining = models.CharField(max_length = 100)
    pan_card_number = models.CharField(max_length = 100)
    skills          = models.TextField(max_length=500)
    about           = models.TextField(max_length=500)
    resume          = models.FileField(upload_to='Resume/')

    def __str__(self):
        return self.first_name


class PayslipMonth(models.Model):
    emplyoee_details = models.ForeignKey(EmployeeDetails, on_delete = models.CASCADE)
    payslip_month    = models.CharField(max_length = 100, unique = True)

    def __str__(self):
        return str(self.payslip_month)


class SalaryDetail(models.Model):
    payslip_month         = models.ForeignKey(PayslipMonth, on_delete = models.CASCADE)
    pay_period            = models.CharField(max_length = 100)
    pay_date              = models.CharField(max_length = 100)
    basic_salary          = models.IntegerField()
    performance_allowance = models.IntegerField()
    bonus_allowance       = models.IntegerField()
    account_number        = models.IntegerField()
    ifsc_code             = models.CharField(max_length = 100)