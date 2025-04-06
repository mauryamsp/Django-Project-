from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    name= models. CharField(max_length= 55)
    email=models.CharField(max_length= 100)
    Question=models.TextField(max_length = 200)
    date=models.DateField(default=timezone.now)
    def _str_(self): 
        return self.name
    


class Enrollment(models.Model): 
    student_id = models.CharField(max_length=45, null=True)
    password = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=55)
    email = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    choose_course = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    fee_status = models.BooleanField(default=False)
    duration = models.IntegerField(default=0)  # Initialize to 0 or null=True
    stu_pic = models.ImageField(upload_to="class_app/student_picture", blank=True, null=True)
    video_url = models.URLField(max_length=200, blank=True, null=True)
    resource_file = models.FileField(upload_to='resources/', blank=True, null=True)

    def __str__(self): 
        return self.name

class trainer(models.Model):
    trainer_id = models.CharField(max_length=50,primary_key=True)   
    password = models.CharField(max_length=50)
    name= models.CharField(max_length=100,default="null")
    phone = models.CharField(max_length=10)
    email= models.EmailField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=4)
    city = models.CharField(max_length=20)
    address = models.TextField(max_length=100)
    experience = models.TextField(max_length=200)
    skills = models.TextField(max_length=100)
    trainer_pic = models.FileField(max_length=100,upload_to="class_app/trainer_images", default=" ")

    def __str__(self): #to represent object in the form of string
        return self.name
    

class course(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    duration = models.IntegerField()
    fees = models.BooleanField()
    syllabus = models.FileField(upload_to='class_app/syllabus',blank=True,null=True)

    def __str__(self):
        return self.name
    

class studyresources(models.Model):
    resource_name = models.CharField(max_length=100)
    resource_file = models.FileField(upload_to='class_app/resourses',blank=True,null=True)
    date = models.DateField()
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.resource_name



class Notice(models.Model):
    notice_content=models.TextField(max_length=100)
    notice_date=models.DateField(default=timezone.now)
    def __str__(self): #to represent object in the form of string
        return self.notice_content
    

class Feedback(models.Model):
    name=models.CharField(max_length=55)
    email=models.EmailField(max_length=50)
    rating=models.CharField(max_length=12)
    review=models.TextField(max_length=100)
    date=models.DateField(default=timezone.now)

    def __str__(self):
     return self.name
    
class Query_Doubts (models.Model):
    name = models. CharField(max_length= 100)
    subject = models.CharField(max_length=100)
    email = models. CharField(max_length= 100)
    member_id=models.CharField(max_length=45,default="")
    question = models.TextField(max_length=150)
    answer = models.TextField(default="")
    question_date = models.DateField(default=timezone.now)
    answer_date = models.DateField(default=None,blank=True,null=True)
    def str(self):
        return self.name
