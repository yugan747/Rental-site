
from django.contrib.gis.db import models 
from geopy.geocoders import Nominatim
from django.contrib.gis.geos import Point

class distance(models.Model):
    Name = models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200)
    Pointlocation=models.PointField(geography=True,null=True,blank=True)



    def save(self,*args, **kwargs):
        if self.Pointlocation is None:
            Search_by_name = Nominatim(user_agent='justtest')
            location = Search_by_name.geocode(self.address)
            if location is not None:
                self.Pointlocation = Point(location.longitude,location.latitude)

            if location is None:
                print('Please enter the valid information')    
    
        super(distance, self).save(*args, **kwargs)    

