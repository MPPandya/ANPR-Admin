from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User,Vehicle
#from django.contrib.admin.models import LogEntry

# Register your models here.
admin.site.site_header="Automatic Number Plate Recognition System"
admin.site.index_title="Welcome to Admin Portal"
admin.site.site_title="Admin Portal"
admin.site.unregister(Group)
#LogEntry.objects.all().delete()

def Send_MSG(modeladmin,request,queryset):
    print(queryset)


class UserAd(admin.ModelAdmin):
    list_display = ('name','mobile_no','email','amount','paymentDone',)
    list_filter =('paymentDone',)
    actions = [Send_MSG]
    search_fields = ('name','email',)

class VehicleAd(admin.ModelAdmin):
    list_display = ('name','number_plate','uid','date')
    list_filter = ('uid',)

admin.site.register(User,UserAd)
admin.site.register(Vehicle,VehicleAd)