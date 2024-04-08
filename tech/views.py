from django.shortcuts import render,redirect
from tech.models import *
from tech.forms import *
from django.contrib.auth import login, authenticate

# Create your views here.
def tech1(request):
    return render(request,"tech1.html")
def javascript5(request):
    return render(request,"javascript5.html")
def jquery(request):
    return render(request,"jquery.html")
def About(request):
    return render(request,"About us.html")
def service(request):
    return render(request,"service.html")
def service(request):
    return render(request,"service.html")
def reg(request):
    return render(request,"reg.html")
   

def fill(request):
    if requst.method=="POST":
        form=customerform(request.post)
        if form.is_valid():
            form.save()
    return render(request.POST)
    

def slider(request):
    return render(request,"slider.html")
def ourteam(request):
    return render(request,"ourteam.html")
def form(request):
    return render(request,"form.html")
def pricing(request):
    return render(request,"pricing.html")    
    
def contact1(request):
    return render(request,"contact.html")
    
def home(request):
    return render(request,"home.html")    
    
def test(request):
    return render(request,"test.html") 
            
def apply(request):
    if request.method=="POST":
        form=contactform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'contact.html')
def counter(request):
    return render(request,"counter.html")

def techblog (request):
    bl=blogs.objects.all()
    context={'bl':bl}
    return render(request,'blog.html',context)
    
def blogdetail(request,id):
    b1=blogs.objects.get(id=id)
    context={'b1':b1}
    return render(request,'blog2.html',context)
    
    
    
def b(request,id):
    em=empt.object.filter(dpt_id=id)
    dept=dpt.object.get(id=id)
    context={'em':em,'dept':dept}
    return render(request,'showemp.html',context)                       
    
    
def showmp(request):
    b=showvideo.objects.all()
    context={'b':b}
    return render(request,'showemp.html',context)
    
def register(request):
    if request.method=="POST":
        form=registerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/paytm/')
            
    return render(request,'registration.html')
def house(request):
    if request.method=="POST":
        form=homeform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'home.html')
    
def partner(request):
    if request.method=="POST":
        form=businessform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'business.html')
def bike(request):
    if request.method=="POST":
        form=car1form(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'car1.html') 

def cmt(request):
    if request.method=="POST":
        form=contactform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'contact.html') 
    
def log(request):
    if request.method=="POST":
        form=loginform(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/login/')
    else:
        form=loginform()
    return render(request,'registration/signup.html',{'form':form})
    
    
def faqs(request):
    fq=faq.objects.all()
    context={'fq':fq}
    return render(request,'faq.html',context)
    
def new1(request):
    fq=faq.objects.all()
    context={'fq':fq}
    return render(request,'new1.html',context)

def insert1(request):
	if request.method=='POST':
		form=registrationform(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/paytm/')
			except:
				pass
	else:
		form=registrationform()
	return render(request,'registration.html',{'form':form})