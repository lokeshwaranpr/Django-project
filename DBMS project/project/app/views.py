from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import Selling
def index(request):
    return render(request,'index.html')

def handlelogin(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        pass1=request.POST.get("pass1")
        myuser=authenticate(username=uname,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentails")
            return redirect('/login')
    return render(request,'login.html')

def handlesignup(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("pass1")
        confirmpassword=request.POST.get("pass2")
        # print(uname,email,password,confirmpassword)
        if password!=confirmpassword:
            messages.warning(request,"Password is Incorrect")
            return redirect('/login')


        try:
            if User.objects.get(username=uname):
                messages.info(request,"UserName Is Taken")
                return redirect('/signup')
        except:
            pass
        try:
            if User.objects.get(email=email):
                messages.info(request,"Email Is Taken")
                return redirect('/signup')
        except:
            pass
    
        myuser=User.objects.create_user(uname,email,password)
        myuser.save()
        messages.success(request,"Signup Success Please login!")
        return redirect('/login')
              
    return render(request,'signup.html')

def sell(request):
    manufacturer_name=request.POST.get("carname")
    manufacture_year=request.POST.get("caryear")
    number_of_seat=request.POST.get("carseats")
    mileage=request.POST.get("carmileage")
    fuel_type=request.POST.get("carfuel")
    carprice=request.POST.get("carprice")
    
    query=sell(carname=manufacturer_name ,caryear=manufacture_year, carseats =number_of_seat ,carfuel=fuel_type ,carmileage=mileage , quote_price=carprice)
    query.save()
    return render(request,'sell.html')
    

def buy(request):
    return render(request,'buy.html')

def sell_car(request):
    if request.method == 'POST':
        manufacturer_name = request.POST.get('carname')
        manufacture_year = request.POST.get('caryear')
        number_of_seats = request.POST.get('carseats')
        fuel_type = request.POST.get('carfuel')
        mileage = request.POST.get('carmileage')
        quote_price = request.POST.get('carprice')

        Selling.objects.create(
            manufacturer_name=manufacturer_name,
            manufacture_year=manufacture_year,
            number_of_seats=number_of_seats,
            fuel_type=fuel_type,
            mileage=mileage,
            quote_price=quote_price
        )
        return redirect('/')
        
    
    return render(request, 'sell_car.html')
def buy_car(request):
    cars = Selling.objects.all()
    return render(request, 'buy_car.html', {'cars': cars})