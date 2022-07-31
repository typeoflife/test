from django.contrib import admin

from backend.models import Client


class ClienAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'operator', 'tag', 'timezone')

admin.site.register(Client, ClienAdmin)