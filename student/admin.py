from django.contrib import admin
from .models import ClassName, Student
from import_export.admin import ImportExportModelAdmin


class ViewAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass


admin.site.register(ClassName, ViewAdmin)
admin.site.register(Student, ViewAdmin)
