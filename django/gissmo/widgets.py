from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime


class DateRangeWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = (AdminSplitDateTime(), AdminSplitDateTime())
        super(DateRangeWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value._lower, value._upper]
        return [None, None]

    def format_output(self, rendered_widgets):
        return '<div class="datetime">' + \
            ' <br /> '.join(rendered_widgets) + '</div>'
