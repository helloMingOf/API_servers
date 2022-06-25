from django.contrib import admin
from Login_servers.models import User
# Register your models here.


admin.site.site_header='花师'
admin.site.site_title='花师系统'
admin.site.index_title='后台主页'
@admin.register(User)
class Users(admin.ModelAdmin):
    list_display=('ID', 'name', 'password', 'region','birthday','picture','gender')
    list_per_page = 5
    ordering = ('ID',)
    list_editable = ['name', 'password']
admin.site.unregister(User)
admin.site.register(User,Users)