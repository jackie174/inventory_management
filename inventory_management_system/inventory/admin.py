from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

# admin.site.register(item)
@admin.register(Volunteers, Participates)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )
