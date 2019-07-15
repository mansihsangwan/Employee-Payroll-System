from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.http import Http404,HttpResponseRedirect, \
                        HttpResponse, HttpResponseForbidden
from django.urls import reverse
from .forms import *


def show_details(request,id):

    employees = EmployeeDetails.objects.get(id=id)

    return render(request,"EmployeeProfile/index.html",{'employees':employees})


def employee_list(request):

    employees = EmployeeDetails.objects.all()
    
    return render(request,"EmployeeProfile/employee_list.html",{'employees':employees})


def create_profile(request):

    if request.method == "POST":

        form = EmployeeDetailsForm(request.POST, request.FILES)
        if form.is_valid():  
            form.save()
            return redirect('EmployeeProfile:employee_list')
      
    else:  
        form = EmployeeDetailsForm()

    return render(request,'EmployeeProfile/create_profile.html',{'form':form}) 


def edit_profile(request, id):

    employee = EmployeeDetails.objects.get(id=id)

    if request.method=='POST':
        form = UpdateEmployeeDetailsForm(request.POST,request.FILES, instance=employee)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('EmployeeProfile:employee_list',args=()))

    form = UpdateEmployeeDetailsForm(instance=employee)

    context = {
        "form":form
    }
    return render(request, 'EmployeeProfile/edit.html', context)


def delete_profile(request, id):

    employee = EmployeeDetails.objects.get(id=id)  
    employee.delete()

    return redirect('EmployeeProfile:employee_list') 


def payslip_month(request, employee_id):

    employee = EmployeeDetails.objects.get(id = employee_id)

    payslipmonth = PayslipMonth.objects.filter(emplyoee_details = employee)

    if request.method == 'POST':
        monthform = MonthForm(request.POST)
        if monthform.is_valid():
            monthform = MonthForm(request.POST)
            new_month = monthform.save()

            return HttpResponseRedirect(reverse('EmployeeProfile:salary_detail',args=(new_month.id,)))

    monthform = MonthForm(initial={'emplyoee_details':employee,})

    context = {
        "monthform":monthform,
        "payslipmonth":payslipmonth,
    }
    return render(request, 'EmployeeProfile/payslip_month.html', context)


def salary_detail(request, month_id):

    payslipmonth = PayslipMonth.objects.get(id = month_id)

    if request.method == 'POST':
        salaryform = SalaryDetailForm(request.POST)
        if salaryform.is_valid():
            salaryform = SalaryDetailForm(request.POST)
            new_salary = salaryform.save()

    salaryform = SalaryDetailForm(initial={'payslip_month':payslipmonth,})

    salaries = SalaryDetail.objects.filter(payslip_month = month_id)

    context = {
        "salaryform":salaryform,
        "salaries":salaries,
    }
    return render(request, 'EmployeeProfile/salary_detail.html', context)


def update_salary_detail(request, salary_id):
    """
    Update Salary
    """
    salary_id = SalaryDetail.objects.get(id = salary_id)

    month_id = salary_id.payslip_month

    if request.method=='POST':
        form = UpdateSalaryDetailForm(request.POST,request.FILES, instance=salary_id)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('EmployeeProfile:salary_detail',args=(month_id.id,)))

    form = UpdateSalaryDetailForm(instance=salary_id)

    context = {
        "form":form
    }
    return render(request, 'EmployeeProfile/update_salary_detail.html', context)


def delete_salary(request, salary_id):
    """
    Delete salary
    """
    salary = SalaryDetail.objects.get(id = salary_id)
    month_id = salary.payslip_month
    # print()
    
    salary_id.delete()

    return HttpResponseRedirect(reverse('EmployeeProfile:salary_detail',args=(month_id.id,)))


def view_slip(request, salary_id):

    salary = SalaryDetail.objects.get(id = salary_id)

    month_id = salary.payslip_month

    employee_id = month_id.emplyoee_details

    employee_details = EmployeeDetails.objects.filter(id = employee_id.id)

    payslip_month = PayslipMonth.objects.filter(id = month_id.id)

    salary_details = SalaryDetail.objects.filter(payslip_month = month_id.id)

    for salary_detail in salary_details:
        # print(employee_detail.basic_salary)
        dearness_allowance = salary_detail.basic_salary/100 * 10
        house_rent_allowance = salary_detail.basic_salary/100 * 8
        travelling_allowance = salary_detail.basic_salary/100 * 6
        food_allowance = salary_detail.basic_salary/100 * 5
        total_balance = salary_detail.basic_salary + salary_detail.performance_allowance + salary_detail.bonus_allowance + dearness_allowance + house_rent_allowance + travelling_allowance + food_allowance

    context = {
        "salary_details":salary_details,
        "employee_details":employee_details,
        "payslip_month":payslip_month,
        "dearness_allowance":dearness_allowance,
        "house_rent_allowance":house_rent_allowance,
        "travelling_allowance":travelling_allowance,
        "food_allowance":food_allowance,
        "total_balance":total_balance
    }
    return render(request, 'EmployeeProfile/view_slip.html', context)