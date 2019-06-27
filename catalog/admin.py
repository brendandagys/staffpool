from django.contrib import admin

# Register your models here.
from catalog.models import Cafeteria, East_Lobby, Town_Centre, CodeStatuses

# admin.site.register(Cafeteria)
# admin.site.register(East_Lobby)
# admin.site.register(Town_Centre)

class CafeteriaAdmin(admin.ModelAdmin):
    list_display = ('c_date', 'c_coordinator')
    list_filter = ['c_date']

    # This removes the 'select multiple and delete selected' functionality, becuase it crashed when used
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(Cafeteria, CafeteriaAdmin)

@admin.register(East_Lobby)
class East_LobbyAdmin(admin.ModelAdmin):
    list_display = ('e_date', 'e_coordinator')
    list_filter = ['e_date']

    # This removes the 'select multiple and delete selected' functionality, becuase it crashed when used
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

@admin.register(Town_Centre)
class Town_CentreAdmin(admin.ModelAdmin):
    list_display = ('t_date', 't_coordinator')
    list_filter = ['t_date']

    # This removes the 'select multiple and delete selected' functionality, becuase it crashed when used
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

@admin.register(CodeStatuses)
class CodeStatuses(admin.ModelAdmin):
    # list_display = ('code_red_status')
    pass
