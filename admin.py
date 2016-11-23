from django.contrib import admin
from models import Clients

class ClientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'mob_no', 'network')


admin.site.register(Clients, ClientsAdmin)
