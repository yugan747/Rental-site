from django.shortcuts import render,redirect

from geopy.geocoders import Nominatim

from .models import distance 
from django.contrib.gis.geos import Point

from django.contrib.gis.measure import Distance 
import folium
from folium.map import Marker




def home(request):
    if request.method == "POST":
        adresses = request.POST['address1']
        print(adresses)
        Get_by_Name = Nominatim(user_agent='justkidding')
        add1 = Get_by_Name.geocode(adresses)
        if add1 is not None:
            pointlocation = Point(add1.longitude,add1.latitude)
            radius = 5
            result=distance.objects.filter(Pointlocation__distance_lt=(pointlocation, Distance(km=radius)))
            counting=distance.objects.filter(Pointlocation__distance_lt=(pointlocation, Distance(km=radius))).count()
            return render(request,'home1.html',{'result':result,'counting':counting})     

        if add1 is None:
            print('wrong')
            return render(request,'home2.html')

       
        




    
    return render(request,'home1.html')        

def badaddress(request):
    return render(request,'home2.html')    

