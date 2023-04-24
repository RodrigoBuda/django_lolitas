from django.contrib import admin
from .models import Usuaria 

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)

admin.site.register(Usuaria, TaskAdmin)