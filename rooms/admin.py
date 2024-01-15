from django.contrib import admin
from rooms.models import Room, Message, RoomCategory

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name','category')

admin.site.register(Room, RoomAdmin)
admin.site.register(Message)
admin.site.register(RoomCategory)