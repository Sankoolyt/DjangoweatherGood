from django.shortcuts import render

# Create your views here.

def home(request):  #define a view, a home view that passes a request
    return render(request,'home.html',{})  # passes the request into the function
## goes to home html and passes in a dictionary later


def about(request): 
    return render(request,'about.html',{})