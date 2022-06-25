from django.contrib import admin
from Article_servers.models import article
# Register your models here.
@admin.register(article)
class Users(admin.ModelAdmin):
    list_display=('ID', 'author', 'time', 'text')
    list_per_page = 5
    ordering = ('ID',)
    list_editable = ['text']
admin.site.unregister(article)
admin.site.register(article,Users)
