from django.contrib import admin
from travels.models import Destination, Vehicle, Travel

# Register your models here.
admin.site.register(Destination)
admin.site.register(Vehicle)
admin.site.register(Travel)