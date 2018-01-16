from django.contrib.postgres.fields import DateTimeRangeField
from django.contrib.postgres.fields import JSONField
from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=254, )

    def __str__(self):
        return '%s' % self.name

    def __unicode__(self):
        return '%s' % self.name


class Model(models.Model):
    SENSOR = 0
    PREAMPLIFIER = 1
    DATALOGGER = 2
    EQUIPMENT = 3
    HYBRID = 4

    name = models.CharField(max_length=254)
    _type = models.ForeignKey(
        'gissmo.Type', related_name='models', on_delete=models.DO_NOTHING)
    chain_type = models.IntegerField(
        choices=((SENSOR, 'Sensor'), (PREAMPLIFIER, 'Preamplifier'),
                 (DATALOGGER,
                  'Datalogger'), (EQUIPMENT, 'Equipment'), (HYBRID, 'Hybrid')))

    def __str__(self):
        return '%s' % self.name

    def __unicode__(self):
        return '%s' % self.name


class Equipment(models.Model):
    name = models.CharField(max_length=254, verbose_name='Serial number')
    model = models.ForeignKey(
        'gissmo.Model', related_name='equipments', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s' % self.name

    def __unicode__(self):
        return '%s' % self.name


class Parameter(models.Model):
    name = models.CharField(max_length=254)
    model = models.ForeignKey(
        'gissmo.Model', related_name='parameters', on_delete=models.DO_NOTHING)
    default = models.ForeignKey(
        'gissmo.Value',
        related_name='is_default',
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True)

    def __str__(self):
        return '%s' % self.name

    def __unicode__(self):
        return '%s' % self.name


class Value(models.Model):
    name = models.CharField(max_length=254)
    parameter = models.ForeignKey(
        'gissmo.Parameter', related_name='values', on_delete=None)

    def __str__(self):
        return '%s' % self.name

    def __unicode__(self):
        return '%s' % self.name


class State(models.Model):
    equipment = models.ForeignKey(
        'gissmo.Equipment', related_name='states', on_delete=models.DO_NOTHING)
    span = DateTimeRangeField(
        verbose_name='Date time range (start/end)',
        help_text='If no end date for the moment, just add start date')
    data = JSONField()

    def __str__(self):
        return '%s - %s' % (self.equipment.name, self.span)

    def __unicode__(self):
        return '%s - %s' % (self.equipment.name, self.span)


class Channel(models.Model):
    name = models.CharField(max_length=254, verbose_name='Ex. FR.CHMF.00.BHZ')
    span = DateTimeRangeField(
        verbose_name='Date time range (start/end)',
        help_text='If no end date for the moment, just add start date')
    states = models.ManyToManyField('gissmo.State')

    def __str__(self):
        return '%s' % self.name

    def __unicode__(self):
        return '%s' % self.name


class Station(models.Model):
    name = models.CharField(max_length=10, verbose_name='Station code')

    def __str__(self):
        return '%s' % self.name


class Place(models.Model):
    name = models.CharField(max_length=254)
    station = models.ForeignKey('gissmo.Station', related_name='places', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.name)