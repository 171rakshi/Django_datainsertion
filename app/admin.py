from django.contrib import admin

# Register your models here.
from app.models import *
class CustomViewWebpage(admin.ModelAdmin):
    list_display=['topic_name','name','url','email']
    list_display_links=['name','url']
    search_fields=['name']
    list_editable=('email',)
    list_filter=['name','url']
    list_per_page=2
admin.site.register(Topic)
admin.site.register(WebPage,CustomViewWebpage)
admin.site.register(AccessRecord)

admin.site.site_header='django2'
admin.site.site_title='project'
admin.site.index_title='Best'