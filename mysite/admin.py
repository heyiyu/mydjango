from django.contrib import admin
from .models import Note
# Register your models here.


class noteAdmin(admin.ModelAdmin):
    list_display = ('nTitle','nCategory','nIsPublic','nCreateTime')
    list_filter = ('nCategory','nCreateTime','nIsPublic')


admin.site.register(Note,noteAdmin)
admin.site.site_header ="后台"
