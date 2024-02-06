import os
from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse

from crms_project import settings
from.forms import CustomerForm, DeathForm, LoginForm, SignUpForm,NINForm
from django.contrib.auth import authenticate, login,logout
from .models import Customer, DeathReg, User
from crms import models
import csv
from django.http import HttpResponse, FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageBreak
from reportlab.lib import colors
from django.template.loader import get_template
from xhtml2pdf import pisa
import qrcode
from django.core.files import File
from django.template import loader
from io import BytesIO



# Create your views here.
# generate PDF file format
def export_to_pdf(request):
    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    employees = Customer.objects.all()

    for employee in employees:
        data = [
            ["NIN:", employee.nin],
            ["First Name:", employee.first_name],
            ["Middle Name:", employee.middle_name],
            ["Last Name:", employee.last_name],
            ["Email:", employee.email],
            ["Gender:", employee.gender],
            ["Date of Birth:", str(employee.dob)],
            ["Registered Date:", str(employee.registered_date)],
            ["Father Name:", employee.fathername],
            ["Mother Name:", employee.mothername],
            ["Address:", employee.address],
            ["District:", employee.district],
            ["City:", employee.city],
            ["Region:", employee.region],
            ["Religion:", employee.religion],
            ["Contact:", employee.contact],
            ["Height:", str(employee.height)],
            ["Citizenship:", employee.citizenship],
        ]

        table = Table(data, colWidths=[100, 400])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), (0.7, 0.7, 0.7)),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), (0.9, 0.9, 0.9)),
            ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),
        ]))

        elements.append(table)
        elements.append(PageBreak())

    doc.build(elements)

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='employee.pdf')







# generate CSV file
def export_to_csv(request):
    employees = Customer.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=employee_details.csv'
    writer = csv.writer(response)
    
    writer.writerow(['NIN', 'FIRST NAME', 'MIDDLE NAME', 'SURNAME', 'EMAIL', 'GENDER','DATE OF BIRTH', 'REGISTERED DATE', 'FATHER NAME', 'MOTHER NAME', 'ADDRESS', 'DISTRICT', 'CITY', 'REGION', 'RELIGION', 'CONTACT', 'HEIGHT', 'CITIZENSHIP', 'PHOTO'])
    
    employee_fields = employees.values_list('nin', 'first_name', 'middle_name', 'last_name', 'email', 'gender', 'dob', 'registered_date', 'fathername', 'mothername', 'address', 'district', 'city', 'region', 'religion', 'contact', 'height', 'citizenship', 'photo')
    
    for employee in employee_fields:
        writer.writerow(employee)
    return response






# home page
def home(request):
    error_message = None  # Initialize the error message to None
    user_info = None

    if request.method == "POST":
        form = NINForm(request.POST)
        if form.is_valid():
            nin = form.cleaned_data['nin']
            try:
                user_info = Customer.objects.get(nin=nin)
                return render(request, 'user_info_model.html', {'user_info': user_info})
            except Customer.DoesNotExist:
                return redirect(reverse('page_404'))
                
        else:
            error_message = "Invalid form data. Please check your input."
    else:
        form = NINForm()

    return render(request, 'index.html', {'form': form, 'user_info': user_info, 'error_message': error_message})


def register(request):
    msg = None
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()  # Save the employee details

            # Redirect to the appropriate URL, e.g., the employee's profile or a success page
            return redirect(reverse('adminstaff_page'))

        else:
            msg = 'Form is not valid'

    return render(request, 'registration.html', {'form': form, 'msg': msg})


# admin delete functions

def delete_staff(request,id):
    employee = User.objects.get(pk=id)
    employee.delete()
    return redirect(reverse('adminstaff_page'))

# staff login page
def index(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None and user.is_admin:
                login(request, user)
                return redirect(reverse('admin_page'))
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect(reverse('employee_page'))
            else:
                msg = 'Invalid credentials please try again'  # Set an error message
        else:
            msg = 'the fields should not be empty'  # Set a different error message for form validation issues

    return render(request, 'login.html', {'form': form, 'msg': msg})



# admin dashoard

def admin_page(request):
    
     total_districts = Customer.objects.values('district').distinct().count()
     total_users = Customer.objects.count()
    # total staff
     total_staff=User.objects.count()

     recent_users = User.objects.all().order_by('-date_joined')[:10]

     male_users = Customer.objects.filter(gender='Male').count()
    
    # Total Female Users
     female_users = Customer.objects.filter(gender='Female').count()

     context = {
       
        'staff_total': total_staff,
        'total_users': total_users,
        'total_districts':total_districts,
        'male_users':male_users,
        'female_users':female_users,
        'recent_users':recent_users,
        
     }

     return render(request,'admin.html',context)
 
def adminstaff_page(request):
     recent_users = User.objects.all().order_by('-date_joined')[:10]
     context = { 
        'recent_users':recent_users, 
     }
     return render(request,'viewstaff.html',context)


# admin add users page
def admin_users(request):
    recent_clients = Customer.objects.all()
    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect(reverse('admin_users'))  # Redirect to a success page
    else:
        form = CustomerForm()
    return render(request,'adusers.html', {'form': form,'recent_clients':recent_clients})

# admin view customer
def view_users(request, pk):
    vuser = Customer.objects.get(id=pk)
    return render(request, 'view_users.html',{'vuser':vuser})

# admin edit employee infor

def update_customer(request, pk):
    customer = Customer.objects.get(id=pk)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()  # Save the updated data to the database
            return redirect(reverse('admin_users'))  # Redirect to a success page
    else:
        form = CustomerForm(instance=customer)

    context = {'form': form, 'customer': customer}
    return render(request, 'update_customer.html', context)


# admin registered death client
def reg_death(request):
    death_records = DeathReg.objects.all()
    total_users = DeathReg.objects.count()
    if request.method == 'POST':
        form = DeathForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect(reverse('reg_death'))  # Redirect to a success page
    else:
        form = DeathForm()
    return render(request, 'admin_death_reg.html',{'death_records': death_records,'form':form,'total_users':total_users})


# qrcode generate page





# empoyee dashboard

def employee_page(request):
     total_districts = Customer.objects.values('district').distinct().count()
     total_users = Customer.objects.count()
     male_users = Customer.objects.filter(gender='Male').count()
     female_users = Customer.objects.filter(gender='Female').count()

     recent_clients = Customer.objects.all()
     if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect(reverse('employee_page'))  # Redirect to a success page
     else:
        form = CustomerForm()
     return render(request,'employee.html', {'form': form,'recent_clients':recent_clients,'total_users': total_users,'total_districts':total_districts, 'male_users':male_users,  'female_users':female_users})

def employeeusers_page(request):
     recent_clients = Customer.objects.all()
     if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect(reverse('employeeusers_page'))  # Redirect to a success page
     else:
        form = CustomerForm()
     return render(request,'employeeusers.html', {'form': form,'recent_clients':recent_clients})

def customer_users(request, pk):
    vuser = Customer.objects.get(id=pk)
    return render(request, 'employee_view.html',{'vuser':vuser})

def emp_update_customer(request, pk):
    customer = Customer.objects.get(id=pk)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()  # Save the updated data to the database
            return redirect(reverse('employeeusers_page'))  # Redirect to a success page
    else:
        form = CustomerForm(instance=customer)

    context = {'form': form, 'customer': customer}
    return render(request, 'employee_update.html', context)


def delete_emp(request,id):
    employee = Customer.objects.get(pk=id)
    employee.delete()
    return redirect(reverse('admin_users'))

def del_client(request, id):
    employee = Customer.objects.get(pk=id)
    employee.delete()
    return redirect(reverse('employeeusers_page'))


def emp_reg_death(request):
    death_records = DeathReg.objects.all()
    total_users = DeathReg.objects.count()
    if request.method == 'POST':
        form = DeathForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect(reverse('reg_death'))  # Redirect to a success page
    else:
        form = DeathForm()
    return render(request, 'employee_death_reg.html',{'death_records': death_records,'form':form,'total_users':total_users})


# user get infromation view
def retrieve_user_info(request):
    if request.method == "POST":
        form = NINForm(request.POST)
        if form.is_valid():
            nin = form.cleaned_data['nin']
            user_info = Customer.objects.get(nin=nin)
            return render(request, 'user_info_modal.html', {'user_info': user_info})
    else:
        form = NINForm()

    return render(request, 'index.html', {'form': form})

# print customer information
def generate_pdf(request, id):
    # Fetch the employee information from the database or any other source
    employee = Customer.objects.get(id=id)

    # Load the HTML template with the employee information
    template = get_template('customerinfo.html')
    html = template.render({'employee': employee})

    # Create a PDF response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Customer_info.pdf"'

    # Generate the PDF using xhtml2pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error generating PDF', content_type='text/plain')

    return response



# display 404 page

def page_404(request):
    return render (request, '404.html')


