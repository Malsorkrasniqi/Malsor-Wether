import urllib.request
import json
from django.shortcuts import render




def index(request):
     
    if request.method == 'POST':
        
        global source 
        try:
            
            city = request.POST['city']   

            source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                            city + '&units=metric&appid=9235bd39b8748d9dc00cae108684f34b')
            
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
            print(data)
            return render(request, "main/index.html", data )
        except : 
            data={"error_message":"error_message"}
            
    return render(request, "main/index.html")
        

   
   