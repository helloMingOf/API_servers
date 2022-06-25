from django.contrib import admin
from mqtt.models import flower_rfid
from mqtt.models import flower
# Register your models here.
@admin.register(flower_rfid)
class Users(admin.ModelAdmin):
    list_display=('id', 'rfid_id', 'time', 'flower_name')
    ordering = ('time',)
    list_filter = ('flower_name',)
    def has_add_permission(self, request):
        # 禁用添加按钮
        return False
    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
admin.site.unregister(flower_rfid)
admin.site.register(flower_rfid,Users)

@admin.register(flower)
class Users2(admin.ModelAdmin):
    list_display=('id', 'flower_name')
admin.site.unregister(flower)
admin.site.register(flower,Users2)