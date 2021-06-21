from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,login,logout
from app.forms import DoctorForm
from app.forms import PatientForm
from app.forms import AppoinmentForm

# Create your views here.
def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')


def Facilities(request):
    return render(request,'facilities.html')


def Home(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors=Doctor.objects.all()
    patients=Patient.objects.all()
    appoinments=Appoinment.objects.all()

    d = 0;
    p = 0;
    a = 0;
    for i in doctors:
        d=d+1
    for i in patients:
        p=p+1
    for i in appoinments:
        a=a+1 

    d1 = {'d':d,'p':p,'a':a}            
    
    return render(request,'home.html',d1)

def view_doctor(request):
    Doctor_list=Doctor.objects.all()
    context={
       "Doctor_list":Doctor_list
    }
    return render(request,'view_doctor.html',context) 

def update_doctor(request,id):
    update_data=Doctor.objects.get(id=id)
    if request.method == "POST":
        form=DoctorForm(request.POST,instance=update_data)
        if form.is_valid():
            form.save()
            return redirect("/view_doctor")
                
    return render(request,"update_doctor.html",{'update_data':update_data})


def delete_doctor(request,id):
    delete_data=Doctor.objects.get(id=id)
    delete_data.delete()
    return redirect("/view_doctor")    


def insert_doctor(request):
    form=DoctorForm()
    if request.method =="POST":
        form=DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/view_doctor")
    return render(request,"insert_doctor.html",{'form':form})

 
                 

def insert_appoinment(request):
    form=AppoinmentForm()
    if request.method =="POST":
        form=AppoinmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/view_appoinment")
    return render(request,"Appoinmentpage.html",{'form':form})  

'''def insert_appoinment(request):
    doctor1=Doctor.objects.all()
    patient1=Patient.objects.all()
    if request.method =="POST":
        d=request.POST['doctor']
        p=request.POST['patient']
        d1=request.POST['date1']
        t=request.POST['time1']
        doctor = Doctor.objects.filter(name=d).first()
        patient = patient.objects.filter(name=p).first()

        Appoinment.objects.Create(doctor=d,patient=p,date1=d1,time1=t)    
        

        d={'doctor':doctor1,'patient':patient1}

        return redirect("/view_appoinment")
        
    
    return render(request,"insert_appoinment.html")'''


def view_appoinment(request):
    appoinment_list=Appoinment.objects.all()
    context={
       "appoinment_list":appoinment_list
    }
    return render(request,'view_appoinment.html',context) 


def delete_appoinment(request,id):
    delete_data=Appoinment.objects.get(id=id)
    delete_data.delete()
    return redirect("/view_appoinment")  


def insert_patient(request):
    form=PatientForm()
    if request.method =="POST":
        form=PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/view_patient")
    return render(request,"insert_patient.html",{'form':form})

def view_patient(request):
    patient_list=Patient.objects.all()
    context={
       "patient_list":patient_list
    }
    return render(request,'view_patient.html',context)

def update_patient(request,id):
    update_data=Patient.objects.get(id=id)
    if request.method == "POST":
        form=PatientForm(request.POST,instance=update_data)
        if form.is_valid():
            form.save()
            return redirect("/view_patient")
                
    return render(request,"update_patient.html",{'update_data':update_data})

def delete_patient(request,id):
    delete_data=Patient.objects.get(id=id)
    delete_data.delete()
    return redirect("/view_patient")  





       
    

def Login(request):
    error=""
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"  
        except:
            error="yes"    
    d = {
        'error':error
        }        
    return render(request,'login.html',d)    

   

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')   


def dumy(request):
    return render(request,'dumy.html')    