from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'home.html')





def login(request):
    print("i am here")
    return render(request,'login.html')



def signup(request):
    return render(request,'signup.html')


def buynow(request):
    return render(request,'buynow.html')

def addcart(request):
    return render(request,'addcart.html')

    
