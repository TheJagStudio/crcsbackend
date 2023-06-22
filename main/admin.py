from django.contrib import admin
from .models import State, District, SocietyType, Application,Society,Bank,Liquidation,User
from import_export.admin import ExportActionMixin
# Register your models here.

class StateAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['stateName', 'stateCode', 'isUt']
    list_editable = ['stateCode']
    search_fields = ['stateName', 'stateCode', 'isUt']

class DistrictAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['districtName', 'districtCode', 'state']
    search_fields = ['districtName', 'districtCode', 'state']

class SocietyTypeAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['societyType','typeCode']
    search_fields = ['societyType','typeCode']
    list_editable = ('typeCode',)

class ApplicationAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ["societyName","state","district","societyType","receivedDate","disposalDate"]
    search_fields = ["societyName","state","district","societyType","receivedDate","disposalDate"]

class SocietyAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ["societyName","Address","state","district","Date","societyType"]
    search_fields = ["societyName","Address","state","district","Date","societyType"]

class BankAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ["bankName","Address","state","district"]
    search_fields = ["bankName","Address","state","district"]

class LiquidationAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ["societyName","state","nameOfLiquidator","appoinmentDate","validityDate","status"]
    search_fields = ["societyName","state","nameOfLiquidator","appoinmentDate","validityDate","status"]

class UserAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ["name","state","district","societyType","date"]
    search_fields = ["name","state","district","societyType","date"]

admin.site.register(State, StateAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(SocietyType, SocietyTypeAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Society, SocietyAdmin)
admin.site.register(Bank, BankAdmin)
admin.site.register(Liquidation, LiquidationAdmin)
admin.site.register(User, UserAdmin)