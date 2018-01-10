from gissmo.models import Equipment
from gissmo.models import Model
from gissmo.models import Type

from django.contrib import admin


class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Type, TypeAdmin)


class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Model, ModelAdmin)


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'model')


admin.site.register(Equipment, EquipmentAdmin)
