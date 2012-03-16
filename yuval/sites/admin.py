__author__ = 'voskov'
from sites.models import pageCMS, GalleryImage
from django.contrib import admin

class pageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date information', {'fields': ['pub_date']}),
        ('Article', {'fields': ['paraName', 'header', 'subHeader', 'para', 'photo']})
    ]


admin.site.register(pageCMS, pageAdmin)

admin.site.register(GalleryImage)