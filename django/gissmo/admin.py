from gissmo.models import Channel
from gissmo.models import Equipment
from gissmo.models import Model
from gissmo.models import Notebook
from gissmo.models import Parameter
from gissmo.models import Place
from gissmo.models import State
from gissmo.models import Station
from gissmo.models import Type
from gissmo.models import Value

from django.contrib import admin


class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', )


class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', )


class StateInline(admin.TabularInline):
    model = State
    extra = 0


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'model')

    inlines = [StateInline]


class ValueInline(admin.TabularInline):
    model = Value
    extra = 2


class ParameterAdmin(admin.ModelAdmin):
    list_display = ('name', 'model')

    inlines = [ValueInline]


class ChannelStateInline(admin.TabularInline):
    model = Channel.states.through
    extra = 2


class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'span')
    fields = ('name', 'span')

    inlines = [ChannelStateInline]


class PlaceInline(admin.TabularInline):
    model = Place
    extra = 1


class NotebookInline(admin.TabularInline):
    model = Notebook
    extra = 0


class StationAdmin(admin.ModelAdmin):
    list_display = ('name', )

    inlines = [PlaceInline, NotebookInline]


admin.site.register(Type, TypeAdmin)
admin.site.register(Model, ModelAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(Channel, ChannelAdmin)
admin.site.register(Station, StationAdmin)
