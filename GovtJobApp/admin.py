from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from GovtJobApp.models import RailwayJobsModel
# Register your models here.

class RailwayJobsAdmin(admin.ModelAdmin):
    list_display = ['company','post_name','education','total_post','location','last_date']

# admin.site.register(RailwayJobsModel,RailwayJobsAdmin)

@admin.register(RailwayJobsModel)
class view(ImportExportModelAdmin):
    pass