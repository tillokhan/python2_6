from django.contrib import admin
from myfiles.models import Portfolio,Category,Services,Team,Contact
# Register your models here.

class AdminPortfolio(admin.ModelAdmin):
    list_display = ['id','name','owner','rasm1']
admin.site.register(Portfolio,AdminPortfolio)


class AdminCategory(admin.ModelAdmin):
    list_display = ['id','name']
admin.site.register(Category,AdminCategory)


class AdminServices(admin.ModelAdmin):
    list_display = ['id','name','rasm']
admin.site.register(Services,AdminServices)


class AdminTeam(admin.ModelAdmin):
    list_display = ['id','desc','name','rasm']
admin.site.register(Team,AdminTeam)

class AdminContact(admin.ModelAdmin):
    list_display = ['name','email','fan','desc','date']




admin.site.register(Contact,AdminContact)

