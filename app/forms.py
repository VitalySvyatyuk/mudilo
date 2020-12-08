import re

from django import forms
from django.utils.translation import gettext as _

from .models import Grievance, Plate
from .plate_regex import regex


class GrievanceForm(forms.ModelForm):
    plate = forms.CharField(
        label=_('License Plate'),
        max_length=30,
        help_text='License plate of the vehicle.')

    def clean_plate(self):
        plate = self.cleaned_data['plate']
        match = re.match(regex['ru'][0], plate)
        if not match:
            raise forms.ValidationError(_('Plate example: а234бв33рус'))
        plate, __ = Plate.objects.get_or_create(name=plate[:8])
        return plate

    class Meta:
        model = Grievance
        fields = ('plate', 'level', 'description')
