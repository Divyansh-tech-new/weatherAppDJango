from django.shortcuts import render
import json 
import urllib.request

# Create your views here.
def index(request):
    if request.method=='POST':
        city=request.POST['city']
        res=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=a7d54081321f281ad7d72c4b99f1e510').read()
        json_data=json.loads(res)
        data={
            "country_code":str(json_data['sys']['country']),
            "coordinate":str(json_data['coord']['lon'])+' '+str(json_data['coord']['lat']),
            "temp":str(json_data['main']['temp'])+'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
    else:   
        data='' 
        city=''
    return render(request,'index.html',{"data":data,"city":city})