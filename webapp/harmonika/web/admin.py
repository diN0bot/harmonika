from django.contrib import admin
from harmonika.web.models import Student, Organization


class StudentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class OrganizationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Student, StudentAdmin)
admin.site.register(Organization, OrganizationAdmin)
