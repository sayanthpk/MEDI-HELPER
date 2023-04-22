from django.db import models

# Create your models here.

class login(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    usertype=models.CharField(max_length=15)

class doctor(models.Model):
    doctorid=models.ForeignKey(login, default=1,on_delete=models.CASCADE)
    doctorname=models.CharField(max_length=20)
    doctorplace=models.CharField(max_length=20)
    doctorpost=models.CharField(max_length=20)
    doctorpin = models.IntegerField()
    email = models.CharField(max_length=20)
    pho_no = models.BigIntegerField()
    qualification=models.CharField(max_length=30)
    category=models.CharField(max_length=30)

class rating(models.Model):
    userid=models.ForeignKey(login,default=1,on_delete=models.CASCADE)
    doctorid = models.ForeignKey(doctor, default=1, on_delete=models.CASCADE)
    rating= models.CharField(max_length=30)

class user(models.Model):
    userid=models.ForeignKey(login, default=1,on_delete=models.CASCADE)
    username=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    phone=models.BigIntegerField()
    email = models.CharField(max_length=20)
    height= models.CharField(max_length=20)
    weight= models.CharField(max_length=20)
    age= models.CharField(max_length=20)

class complaints(models.Model):
    userid = models.ForeignKey(user, default=1, on_delete=models.CASCADE)
    complaints=models.CharField(max_length=20)
    complaint_date =models.CharField(max_length=200)
    reply=models.CharField(max_length=20)
    reply_date=models.CharField(max_length=20)


class schedule(models.Model):
    doctorid = models.ForeignKey(doctor, default=1, on_delete=models.CASCADE)
    tocken_count=models.IntegerField()
    schedulingtime=models.TimeField()
    schedulingdate = models.DateField()


class booking(models.Model):
    userid = models.ForeignKey(user, default=1, on_delete=models.CASCADE)
    schedule_id=models.ForeignKey(schedule, default=1, on_delete=models.CASCADE)
    date=  models.CharField(max_length=20)
    tocken_no=models.IntegerField()


class chat(models.Model):
    doctor_id= models.ForeignKey(doctor, default=1, on_delete=models.CASCADE)
    user_id=models.ForeignKey(user, default=1, on_delete=models.CASCADE)
    date=models.CharField(max_length=20)
    type= models.CharField(max_length=20)
    message= models.CharField(max_length=20)


