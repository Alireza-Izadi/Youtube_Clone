from django.contrib import admin
from userauths.models import User
from import_export.admin import ImportExportModelAdmin

class UserAdmin(ImportExportModelAdmin):
    pass
# Register your models here.

admin.site.register(User, UserAdmin)