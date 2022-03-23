from audioop import add
from email import message
import email
from django.contrib.auth import authenticate
# from pyexpat.errors import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login
from jewelleryshop.models import About, Blog, Carausal, Info, Offer, Shop, Shopcat, Testimonial,Contact,Item
from django.contrib import messages


# from . models import
# Create your views here.

def index(request):
    shopcat=Shopcat.objects.all()
    carausal=Carausal.objects.all()
    shop=Shop.objects.all()
    about=About.objects.all()
    offer=Offer.objects.all()
    blog=Blog.objects.all()
    testimonial=Testimonial.objects.all()
    info=Info.objects.all()
    context ={
        'cat':shopcat,
        'carausal':carausal,
        'shop':shop,
        'about':about,
        'offer':offer,
        'blog':blog,
        'testimonial':testimonial,
        'info':info
    }
    
    return render(request,'index.html',context)

def jwellery(request,slug):
    shop=Shop.objects.filter(slug=slug)
    context ={
        
        'shop':shop,
        
    }
    
    return render(request,'jwellery.html',context)

def about(request):    
    about=About.objects.all()
    shopcat=Shopcat.objects.all()
    context={
            'about':about,
            'cat':shopcat,
            
    }
      
    return render(request,'about.html',context) 

def shop(request):    
    shop=Shop.objects.all()
    shopcat=Shopcat.objects.all()
    context={
            'shop':shop,
            'cat':shopcat,
    }
      
    return render(request,'shop.html',context) 


def details(request,slug):    
    shop=Shop.objects.filter(slug=slug)
    context={
            'shop':shop
    }
      
    return render(request,'details.html',context) 


def blog(request):    
    blog=Blog.objects.all()
    shopcat=Shopcat.objects.all()
    context={
            'blog':blog,
            'cat':shopcat,
    }
      
    return render(request,'blog.html',context) 


def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message=request.POST.get('message')
        
        if len(name)<2 or len(email)<3 or len(message)<10:
            messages.error(request,"please fill the form correctly...")
        else:    
            contact=Contact(name=name,email=email,message=message)
            contact.save()
            messages.success(request,"Your massage has been sucessully sent ")
            
            return redirect('/')
    return render(request,"contact.html")


def userlogin(request):
    if request.method  == "POST":
        username = request.POST['username']
        password =  request.POST['password']
        user=authenticate(username=username,password = password)
        if user is not None:
            login(request,user)
            messages.success(request,'sucessfully logged in')
            return redirect('/')
        else:
            messages.error(request,'user is not valid')
            return redirect('/userlogin')
    return render (request,'userlogin.html') 
        
def shopcat(request,slug):    
    shop=Shop.objects.all()
    shopcat=Shop.objects.all()
    cat=Shop.objects.all(slug=slug)
    product=Shop.objects.filter(shopcat=cat)
    context={
            'shop':shop,
            'cat':shopcat,
            'pro':product
            }
      
    return render(request,'shop.html',context) 

def add_to_cart (request):
    return render(request,'add_to_cart.html')



def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "product.html", context)

    
        