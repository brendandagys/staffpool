from django.contrib import admin

# Register your models here.
from chat.models import Messages

@admin.register(Messages)
class Messages(admin.ModelAdmin):
    readonly_fields = ('timestamp',)
