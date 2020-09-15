from django.contrib import admin
from .models import Myuser

class MyuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'registered_dttm')

admin.site.register(Myuser, MyuserAdmin)  