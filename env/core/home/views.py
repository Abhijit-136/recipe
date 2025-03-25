from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    people=[{'name':"Abhijit",'age':21},
            {'name':"Abhi",'age':26},
            {'name':"jit",'age':24},
            {'name':"Ankit",'age':28},
            {'name':"Aliit",'age':27}            
            
            ]
    return render(request,"index.html",context={'people':people})

def sucess_page(request):
    return HttpResponse("home/<h1> this is a sucess page<h2>")


def about_page(request):
    return render(request, "about.html")

def contact_page(request):
    context={'page':'contact'}
    return render(request, "contact.html",context)
