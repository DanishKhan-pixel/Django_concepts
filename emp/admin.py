from django.contrib import admin
from .models import *
# Register your models here.


class EmpAdmin(admin.ModelAdmin):
    list_display=('name',"working","emp_id","department","phone")
    list_editable=("working","phone")
    search_fields=("name",)
    list_filter=("working",)

admin.site.register(Emp,EmpAdmin)
admin.site.register(Testimonial)