from django.contrib import admin

from schoolapp.models import Department, Course, Details,Purpose

# Register your models here.
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Details)
admin.site.register(Purpose)
