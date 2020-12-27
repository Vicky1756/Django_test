from django.contrib import admin
from .models import School,Student

admin.site.site_header = 'Schools Administration'

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'max_student','location')
    
class StudentAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'school' )
    admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)