from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import customer
from .models import Transaction
from django.http import JsonResponse

def indexview(request):
    return render(request,"myapp/index.html")
def loginview(request):
    return render(request,"myapp/user_login.html")
def regisview(request):
    return render(request,"myapp/user_registration.html")
def insertviews(request):
    if request.method == 'POST':
       name=request.POST['name']
       email=request.POST['email']
       password=request.POST['password']
       contact=request.POST['phone']
       dob=request.POST['dob']
       gender=request.POST['gender']
       #validate for user already exit or not
       user=customer.objects.filter(Email=email)
       if user:
           message=": User already exit :"
           return render(request,"myapp/user_registration.html",{'msg':message})
       else:
           newuser=customer.objects.create(Name=name,Email=email,Password=password,Contact=contact,Dob=dob,Gender=gender)
           message=": Succesfully register  :"
           return render(request,"myapp/user_login.html",{'msg':message})
        #else:
           # message="User not found please register"
           # return render(request,"myapp/user_registration.html",{'msg':message})
def user_logviews(request):
    return render(request,"myapp/index.html")
def user_profileview(request):
    return render(request,"myapp/profile.html")
def after_loginhomeview(request):
    return render(request,"myapp/user_home.html")
def send_moneyview(request):
    return render(request,"myapp/s_money.html")
def t_hisview(request):
    return redirect('transaction_history') 
def upi_view(request):
    return render(request,"myapp/upi.html")
def bank_transferview(request):
    return render(request,"myapp/sent_to_bank.html")
def deposite_moneyview(request):
    return render(request,"myapp/deposit.html")


def user_loginview(request):
    if request.method == 'POST':
        Email=request.POST['email']
        password=request.POST['password']
        # Check email and password from database
        try:
            user = customer.objects.get(Email=Email)
        except customer.DoesNotExist:
            message = "User does not exist. Please register."
            return render(request, "myapp/user_registration.html", {'msg': message})
        if user.Password == password:
            request.session['Name'] = user.Name
            request.session['Email'] = user.Email
            request.session['Dob'] = user.Dob
            request.session['Gender'] = user.Gender
            request.session['Contact'] = user.Contact
            request.session['Balance'] = int(user.Balance)
            return render(request, "myapp/user_home.html")
        else:
            message = "Password does not match."
            return render(request, "myapp/user_login.html", {'msg': message})
def bank_payment(request):
    if request.method == 'POST':
        # Handle form submission here
        bank_details = request.POST.get('bank_details')
        Acount_number = request.POST.get('Acount_number')
        Ifsc_code = request.POST.get('Ifsc_code')
        bank_amount = int(request.POST.get('bank_amount'))
        user_email = request.session.get('Email')
        user = customer.objects.get(Email=user_email)
        # Deduct payment amount from user's balance
        if int(user.Balance) < bank_amount:
            msg = "Payment failed: insufficient balance."
        else:
            user.Balance -= bank_amount
            user.save()
            request.session['Balance'] = user.Balance
            msg = "Payment successful!"
            # create Transaction object for bank payment
            Transaction.objects.create(
                user=user,
                payment_method='Bank Transfer',
                payment_details=f"Account Number: {Acount_number}, IFSC Code: {Ifsc_code}",
                transaction_type='Debit',
                amount=bank_amount
            )
    else:
        # Display form for UPI payment
        msg = ""

    return render(request, "myapp/sent_to_bank.html", {'msg': msg})

def upi_payment(request):
    if request.method == 'POST':
        # Handle form submission here
        upi_details = request.POST.get('upi_details')
        upi_amount = int(request.POST.get('upi_amount'))
        user_email = request.session.get('Email')
        user = customer.objects.get(Email=user_email)
        # Deduct payment amount from user's balance
        if int(user.Balance) < upi_amount:
            msg = "Payment failed: insufficient balance."
        else:
            user.Balance -= upi_amount
            user.save()
            request.session['Balance'] = user.Balance
            msg = "Payment successful!"
            # create Transaction object for UPI payment
            Transaction.objects.create(
                user=user,
                payment_method='UPI',
                payment_details=upi_details,
                transaction_type='Debit',
                amount=upi_amount
            )
    else:
        # Display form for UPI payment
        msg = ""

    return render(request, "myapp/upi.html", {'msg': msg})

def deposite_paymet(request):
    if request.method == 'POST':
        # Handle form submission here
        amount = int(request.POST.get('amount'))
        user_email = request.session.get('Email')
        user = customer.objects.get(Email=user_email)
        # Deduct payment amount from user's balance
        if amount <= 0:
            msg = "Enter a valid amount"
        else:
            user.Balance += amount
            user.save()
            request.session['Balance'] = user.Balance
            msg = "Payment successful!"
            # create Transaction object for deposit payment
            Transaction.objects.create(
                user=user,
                payment_method='Deposit',
                payment_details='Credit Amount to Self',
                transaction_type='Credit',
                amount=amount
            )
    else:
        # Display form for deposit payment
        msg = ""

    return render(request, "myapp/deposit.html", {'msg': msg})

def transaction_history(request):
    user_email = request.session.get('Email')
    user = customer.objects.get(Email=user_email)
    transactions = Transaction.objects.filter(user=user).order_by('-id')
    return render(request, "myapp/T_his.html", {'transactions': transactions})
