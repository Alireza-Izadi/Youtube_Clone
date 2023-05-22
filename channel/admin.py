from django.contrib import admin
from channel.models import Channel
from import_export.admin import ImportExportModelAdmin

class ChannelAdmin(ImportExportModelAdmin):
    list_display = ["channel_name", "user", "status"]
# Register your models here.
admin.site.register(Channel, ChannelAdmin)