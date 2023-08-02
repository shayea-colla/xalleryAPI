from django.contrib import admin

from gallery.models import Picture, Room

# Register your models here.
admin.site.register(Picture)


class RoomAdmin(admin.ModelAdmin):
    pass


admin.site.register(Room, RoomAdmin)
