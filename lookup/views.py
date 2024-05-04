from django.shortcuts import render

# Create your views here.

def home(request):  #define a view, a home view that passes a request
    import json
    import requests
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=F60FDB8C-6F1F-412E-BD6D-2A84E235CE44")
    try:
        api = json.loads(api_request.content)

    except Exception as e:
        api = "Error EN LA PUTA BASE DE DATOS"
    return render(request,'home.html',{'api':api})  # passes the request into the function
## goes to home html and passes in a dictionary later


def about(request): 
    return render(request,'about.html',{})