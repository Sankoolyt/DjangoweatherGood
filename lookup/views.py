from django.shortcuts import render

# Create your views here.

def home(request):  #define a view, a home view that passes a request
## goes to home html and passes in a dictionary later
    import json
    import requests
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=F60FDB8C-6F1F-412E-BD6D-2A84E235CE44")
    try:
        api = json.loads(api_request.content)

    except Exception as e:
        api = "Chiiispas, something went wrong"
    if api[0]['Category']['Name'] == "Good":  ## sets a conditional when the output comes out and links it onto the corresponding html class
        category_description = 'Esta con madre el clima y puedes hacer cosas chingonas'
        category_color='good'   # html classes are on the base html file and are referenced here
    elif api[0]['Category']['Name'] == "Moderate":
        category_description ='Cámara mi tibio, toma agua y ponte pilas para que no te me desmayes'
        category_color='moderate'
    elif api[0]['Category']['Name'] == "USG":
            category_description ='Anda de viva la contaminación, pero no te dejes mi tibio'
            category_color='usg'
    elif api[0]['Category']['Name'] == "Unhealthy":
        category_description ='Se está poniendo al tiro el clima, tú sal con tapaocicos y ya andas gucci'
        category_color='unhealthy'
    elif api[0]['Category']['Name'] == "Very Unhealthy":
        category_description ='Estos niveles de contaminación  son generados por los neoliberales '
        category_color='veryunhealthy'
    elif api[0]['Category']['Name'] == "Hazardous":
        category_description ='no es por alarmarte pero mejor vete del país que anda insano en clima'
        category_color='hazardous'
    return render(request,'home.html',{'api': api,
                                       "category_description":category_description,
                                       "category_color": category_color }) # passes the request into the function

def about(request): 
    return render(request,'about.html',{})