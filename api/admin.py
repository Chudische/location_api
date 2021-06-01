from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from .models import Place

class PlaceResource(resources.ModelResource):
    class Meta:
        model = Place
        fields = ('id', 'parent_id', 'category', 'name')

class PlaceAdmin(ImportExportModelAdmin):
    resource_class = PlaceResource
    list_display = ('id', 'parent_id', 'category', 'name', '__str__','is_location')
    search_fields = ( 'id','name')
    list_filter = ('is_location',)

admin.site.register(Place, PlaceAdmin)