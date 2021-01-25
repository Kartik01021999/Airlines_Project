from django.contrib import admin
from .models import flights
from .models import Booking
# Register your models here
admin.site.register(flights)
admin.site.register(Booking)
