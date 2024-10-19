from django.contrib import admin
from .models import Airport,Flight,Passenger

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id","origin","destination","duration")
class PasengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flight",)


admin.site.register(Airport)
admin.site.register(Flight,FlightAdmin)
admin.site.register(Passenger,PasengerAdmin)
# Register your models here.
