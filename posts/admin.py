from django.contrib import admin
from .models import Post
from branches.models import Journal

from import_export import resources, fields,widgets
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class PostResource(resources.ModelResource):

    title = fields.Field(attribute='title',column_name='Title')
    authors = fields.Field(attribute='authors',column_name='Authors')
    summary = fields.Field(attribute='summary',column_name='Summary')
    link = fields.Field(attribute='link',column_name='Link')
    date = fields.Field(attribute='date',column_name='Date')
    journal = fields.Field(attribute='journal',column_name='Journal',widget=widgets.ForeignKeyWidget(Journal, 'name'))
    type = fields.Field(attribute='type',column_name='Category')

    class Meta:
        model = Post
        fields = ('id','title','authors','summary','link','date','journal','type')

class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PostResource

admin.site.register(Post,PostAdmin)
