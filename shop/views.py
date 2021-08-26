from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact, Product
from math import ceil
# Create your views here.
def index(request):
    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides= n//4 + ceil((n/4) + (n//4))
        allProds.append([prod, range(1,nSlides),nSlides])
    params={'allProds':allProds}
    return  render(request,'shop/index.html' ,params)
def about(request):
    return render(request,'shop/about.html')
def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        print(name,email,phone, desc )  
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return  render(request,'shop/contact.html')
def tracker(request):
    return  render(request,'shop/tracker.html')
def search(request):
    return  render(request,'shop/search.html')
def products(request,my_id):
    print(my_id)
    product=Product.objects.filter(id=my_id)
    print(product)
    params={'prod':product}
    return render(request, "shop/prodView.html",params)
def checkout(request):
    return  render(request,'shop/checkout.html')
