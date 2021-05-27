from django.contrib import admin
from .models import Userreg
from .models import add_bus, createpass
from import_export.admin import ImportExportModelAdmin


# Register your models here.


class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['user_id', 'uname', 'pwd', 'DOB', 'age', 'address', 'gender', 'mobile', 'uemail']
admin.site.register(Userreg, UserAdmin)

class AdminAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['busno', 'location', 'to', 'amount', 'stop1', 'stop2', 'stop3', 'stop4']
admin.site.register(add_bus, AdminAdmin)

class CreatePass(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'user_id', 'Busno', 'full_name', 'From', 'To', 'Date1', 'Date2', 'amount', 'profile_pic', 'cc_number', 'cvv', 'expiry', 'month', 'qr_codes']
admin.site.register(createpass, CreatePass)