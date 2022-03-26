
from django.contrib.gis import admin

from .models import distance

admin.site.register(distance,admin.GISModelAdmin)