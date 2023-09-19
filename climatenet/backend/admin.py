from django.contrib import admin
from backend.models import Devices  


# Customize the admin site title and header
admin.site.site_title = "ClimateNet Admin"
admin.site.site_header = "CliamteNet Admin"


class DeviceDetailsAdmin(admin.ModelAdmin):
    readonly_fields = ('country',)  # Make the 'country' field read-only

admin.site.register(Devices, DeviceDetailsAdmin)
