from django.contrib import admin
from . import models

from import_export.admin import ImportExportModelAdmin
from import_export import resources

admin.site.site_title = 'BitGrow Administration'
admin.site.site_header = 'BitGrow Administration'
admin.site.index_title = 'BitGrow Administration'


class KOLResource(resources.ModelResource):
    class Meta:
        model = models.KOL


class KOLAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [KOLResource]
    list_display = ('name', 'intro', 'avatar', 'quoted_price',
                    'connectable_user', 'language', 'area', 'average_display',
                    'total_reward', 'claim_reward', "address")


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'intro', 'avatar',
                    'website', 'twitter', 'discord', 'contract']

    class Meta:
        model = models.Project


class TaskAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'project', 'platform', 'area', 'delivery_method', 'price', 'fans_requirement',
                    'requirement', 'text', 'status']

    class Meta:
        model = models.Task


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_id', 'task', 'kol',
                    'price', 'status', 'verify_url']

    class Meta:
        model = models.Order


admin.site.register(models.KOL, KOLAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Task, TaskAdmin)
admin.site.register(models.Order, OrderAdmin)
