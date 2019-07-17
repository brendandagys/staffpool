from django.contrib import admin

# Register your models here.
from catalog.models import Cafeteria, East_Lobby, Town_Centre, CodeStatuses, IncidentCommander, CodeBlue

from import_export.admin import ImportExportModelAdmin
from import_export import resources


class CafeteriaResource(resources.ModelResource):
    class Meta:
        model = Cafeteria

class East_LobbyResource(resources.ModelResource):
    class Meta:
        model = East_Lobby

class Town_CentreResource(resources.ModelResource):
    class Meta:
        model = Town_Centre

class IncidentCommanderResource(resources.ModelResource):
    class Meta:
        model = IncidentCommander

class CodeBlueResource(resources.ModelResource):
    class Meta:
        model = CodeBlue


@admin.register(Cafeteria)
class CafeteriaAdmin(ImportExportModelAdmin):
    resource_class = CafeteriaResource
    list_display = ('c_date', 'c_coordinator')
    list_filter = ['c_date']

    # This removes the 'select multiple and delete selected' functionality, becuase it crashed when used
    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions

# admin.site.register(Cafeteria, CafeteriaAdmin)

@admin.register(East_Lobby)
class East_LobbyAdmin(ImportExportModelAdmin):
    resource_class = East_LobbyResource
    list_display = ('e_date', 'e_coordinator')
    list_filter = ['e_date']


@admin.register(Town_Centre)
class Town_CentreAdmin(ImportExportModelAdmin):
    resource_class = Town_CentreResource
    list_display = ('t_date', 't_coordinator')
    list_filter = ['t_date']


@admin.register(CodeStatuses)
class CodeStatusesAdmin(admin.ModelAdmin):
    readonly_fields = ('code_timestamp',)


@admin.register(IncidentCommander)
class IncidentCommanderAdmin(ImportExportModelAdmin):
    resource_class = IncidentCommanderResource
    list_display = ('i_date', 'i_time')
    list_filter = ['i_date']


@admin.register(CodeBlue)
class CodeBlueAdmin(ImportExportModelAdmin):
    resource_class = CodeBlueResource
    list_display = ('blue_date', 'blue_time')
    list_filter = ['blue_date']
