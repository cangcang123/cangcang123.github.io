from django.contrib import admin
from .models import Products,Giohang
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'date']
    list_filter = ['date']
    search_fields = ['name','id']
admin.site.register(Products,PostAdmin)
admin.site.register(Giohang,PostAdmin)
