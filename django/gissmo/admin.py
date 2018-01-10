from gissmo.models import Equipment
from gissmo.models import Model
from gissmo.models import Parameter
from gissmo.models import Type
from gissmo.models import Value

from django.contrib import admin


class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', )


class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', )


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'model')


class ValueInline(admin.TabularInline):
    model = Value
    extra = 2


class ParameterAdmin(admin.ModelAdmin):
    list_display = ('name', 'model')

    inlines = [ValueInline]


admin.site.register(Type, TypeAdmin)
admin.site.register(Model, ModelAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Parameter, ParameterAdmin)
