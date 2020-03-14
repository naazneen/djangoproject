from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from .models import Student
from import_export.admin import ImportExportModelAdmin


admin.site.unregister(Group)

class StudentAdmin(ImportExportModelAdmin):
    list_display_links = ('firstname',)
    list_display = ('firstname','lastname','email','gender')
    list_editable = ('email',)
    list_filter = ('gender','date_added',)
    search_fields = ('firstname','lastname','email','gender')
    
admin.site.register(Student,StudentAdmin)
""""    
class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource

admin.site.register(Book, BookAdmin)"""