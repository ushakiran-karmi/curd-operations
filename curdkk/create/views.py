from django.shortcuts import redirect, render
from .models import User

#from . models import Use


# Create your views here.

#to create the userregister page
def userreg(request):
    return render(request,"create/user.html",{})


#create the insert method
def insertuser(request):
    vuid=request.POST['tuid'];#post uid most be same with html uid
    vuname=request.POST['tuname'];
    vuemail=request.POST['tuemail'];
    vucontact=request.POST['tucontact'];
    us=User(uid=vuid, uname=vuname, uemail=vuemail, ucontact=vucontact);#
    us.save();
    return render(request,'create/user.html',{})
    


#create a view in view.py for viewuser.html to fetch data from database

def viewuser(request):
    user=User.objects.all()  #user must be same with table name
    return render(request,"create/viewuser.html",{'userdata':user})   # user and userdata of user must be same

#create a view in view.py to delete data ta database

def deleteprofile(request, id):
    us=User.objects.filter(uid=id)       #udi should match with database colunm uid and id match with request id
    us.delete()                       #to delete the multiple same data we use filter()or if we want to delete the one id we use get()
    return redirect("/view")

def editprofile(request, id):
    user =User.objects.get(uid=id)
    return render(request,"create/edit.html",{'user':user})

def updateprofile(request,id):
    newuid=request.POST['uid']
    newuname=request.POST['uname']
    newuemail=request.POST['uemail']
    newucontact=request.POST['ucontact']
    user=User.objects.get(uid=id)
    user.uid=newuid
    user.uname=newuname
    user.uemail=newuemail
    user.ucontact=newucontact
    user.save()
    return redirect("/view")
    
    
    
    
    
    


