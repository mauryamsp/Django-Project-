from django.shortcuts import render,redirect,HttpResponse
from .models import Contact,Enrollment,Notice
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'class_app/html/index.html')#template rendering in django

def about(request):
    return render(request,'class_app/html/about_us.html')
# Assuming you've defined the Contact class and set up your database

def contact(request):

    if request.method=="POST":#http protocol sends user data using POST method
         user_name=request.POST["name"]#request.POST[]built-in dictionary 
         user_email  =request.POST["email"]
         user_question=request.POST["question"]
         #print(user_name,user_email,,user_question)
         contact_obj=Contact(name=user_name,email=user_email,Question=user_question)#creating Contact class object
         contact_obj.save()#ORM map with contact table fields
         messages.success(request,"❤️❤️❤️Thanku for contacting us We will reach you soon❤️❤️❤️")
    
         return redirect("contact")#it is logical name of the view 
    return render(request,'class_app/html/contact.html')

def courses(request):
    return render(request,'class_app/html/courses.html')

def mentors(request):
    return render(request,'class_app/html/mentors.html')

def python(request):
    return render(request,'class_app/html/python.html')

def machine_learning(request):
    return render(request,'class_app/html/machine_learning.html')


def core_java(request):
    return render(request,'class_app/html/core_java.html')

def advance_java(request):
    return render(request,'class_app/html/advance_java.html')

def android(request):
    return render(request,'class_app/html/android.html')

def iot(request):
    return render(request,'class_app/html/iot.html')

def faq(request):
    return render(request,'class_app/html/faq.html')



def registration(request):
    if request.method=="GET":
        return render(request, 'class_app/member/member_registration.html')
    
    if request.method=="POST":
        name=request.POST["name"]
        phone=request.POST["phone"]
        email=request.POST["email"]
        # mem_gender=request.POST["gender"]
        city=request.POST["city"]
        address=request.POST["address"]
        pic=request.FILES["profile_pic"]
        obj=Enrollment(name=name,phone=phone,email=email,city=city,address=address,stu_pic=pic)
        obj.save()
        return redirect("member_registration")
    
def home(request):
   
    notice_list=Notice.objects.all()

    context={
        "notice_key":notice_list,
    }

    return render(request,'class_app/html/index.html',context)

