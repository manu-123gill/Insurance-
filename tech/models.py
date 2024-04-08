from django.db import models

# Create your models here
class saveform(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    message=models.CharField(max_length=100)
    subject=models.CharField(max_length=100,default='true')
    
class blogs(models.Model):
    title=models.CharField(max_length=50)
    date=models.DateField()
    des=models.TextField()
    image=models.ImageField(upload_to='pictures')
    class Meta:
        db_table='blogs'

class loginform(models.Model):
    Password=models.CharField(max_length=40)
    email=models.EmailField(max_length=30)
    
class contact(models.Model):
    Name=models.CharField(max_length=40)
    email=models.EmailField(max_length=30)
    Subject=models.CharField(max_length=30)
    Message=models.CharField(max_length=30)
    class Meta:
        db_table='contact'
    
class dpt(models.Model):
    name=models.CharField(max_length=20)
    
class homeform(models.Model):
    location=models.CharField(max_length=40)
    Area=models.CharField(max_length=30)    
    floors=models.CharField(max_length=30) 
    
class businessform(models.Model):
     Business=models.CharField(max_length=30)
     Type=models.CharField(max_length=30)
     location=models.CharField(max_length=30)
     Area=models.CharField(max_length=30)    
     floors=models.CharField(max_length=30)    
     
class car1form(models.Model):
     Company=models.CharField(max_length=30)
     Model=models.CharField(max_length=30)
     color=models.CharField(max_length=30)
     registrationdate=models.CharField(max_length=30)    
     number=models.CharField(max_length=30)     
    
class empt(models.Model):
    name=models.CharField(max_length=20)
    salary=models.IntegerField()
    dpt_id=models.ForeignKey(dpt,on_delete=models.CASCADE)
    class Meta:
        db_table='empt'
        
class showvideo (models.Model):
    image=models.CharField(max_length=300)
    video=models.CharField(max_length=300)
    class Meta:
        db_table='showvideo'
        
class registrationform(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=30)
    address=models.TextField()
    city=models.CharField(max_length=30)
    pin=models.IntegerField()
    adhar_no=models.IntegerField()
    class Meta:
        db_table='registrationform'
    
class faq(models.Model):
        que=models.TextField()
        ans=models.TextField()
        class Meta:
           db_table='faq'