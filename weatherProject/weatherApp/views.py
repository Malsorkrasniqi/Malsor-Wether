import urllib.request
import json
import pycountry
from django.shortcuts import render


def index(request):
    if request.method == 'POST':    
        try:
            city = request.POST['city'] 

            source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+
                                         city.replace(" ", "%20")+'&units=metric&appid=9235bd39b8748d9dc00cae108684f34b')
            
            list_of_data = json.loads(source.read())

            data = { 
                "country_code": str(list_of_data['sys']['country']),
                "wind": str(list_of_data['wind']['speed']),
                "temp": str(list_of_data['main']['temp']) + ' °C',
                "pressure": str(list_of_data['main']['pressure']),  
                "humidity": str(list_of_data['main']['humidity']),
                'main': str(list_of_data['weather'][0]['main']),
                'description': str(list_of_data['weather'][0]['description']),
                'icon': list_of_data['weather'][0]['icon'],
                
            }

            # Extract the country code from the API response
            country_code = str(list_of_data['sys']['country'])

            # Use pycountry to get the country name from the country code
            country_name = pycountry.countries.get(alpha_2=country_code).name

            # Add the country name to the data dictionary
            data["country_name"] = country_name

            print(data)
            return render(request, "main/index.html", data)
        except:
            data = {"error_message": "error_message"}

    return render(request, "main/index.html")


