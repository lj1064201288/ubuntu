from django.contrib import admin

from .models import *
# Register your models here.

class ProducrAdmin(admin.ModelAdmin):
    list_display = ('pmodel', 'nikename', 'price', 'year',)
    search_fields = ('nikename',)

    ordering = ('-price',)


admin.site.register(Product, ProducrAdmin)
admin.site.register(Maker)
admin.site.register(PPhoto)
admin.site.register(Pmodel)