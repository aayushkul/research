from django.contrib import admin
from .models import Branch,Journal
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class BranchResource(resources.ModelResource):

    name = fields.Field(attribute='name',column_name='Name')

    class Meta:
        model = Branch
        fields = ('id','name',)

class BranchAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = BranchResource


admin.site.register(Branch,BranchAdmin)
admin.site.register(Journal)
