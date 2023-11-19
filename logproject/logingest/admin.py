from django.contrib import admin
from logingest.models import *

class LogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Log, LogAdmin)

