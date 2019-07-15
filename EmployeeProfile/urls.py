from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'EmployeeProfile'

urlpatterns = [
    path('show_details/<int:id>',show_details,name='show_details'),
    path('', employee_list, name='employee_list'),
    path('add_details/', create_profile, name="create_profile"),
    path('delete/<int:id>', delete_profile, name='delete_profile'),
    path('edit/<int:id>', edit_profile, name="edit_profile"),
    path('payslip_month/<int:employee_id>', payslip_month, name = 'payslip_month'),
    path('salary_detail/<int:month_id>', salary_detail, name = 'salary_detail'),
    path('update_salary_detail/<int:salary_id>', update_salary_detail, name = 'update_salary_detail'),
    path('delete_salary/<int:salary_id>', delete_salary, name = 'delete_salary'),
    path('view_slip/<int:salary_id>', view_slip, name = 'view_slip'), 
]                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                         