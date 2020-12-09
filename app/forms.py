from django import forms
from django.utils.translation import gettext as _

from .models import Grievance, Plate
from .utils import validate_plate, map_words, clean_p


class GrievanceForm(forms.ModelForm):
    plate = forms.CharField(
        label='',
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': _('Example: A324BK 23rus')}),
        help_text=_('License plate of the vehicle'))
    level = forms.IntegerField(
        label='',
        initial=3,
        min_value=1,
        max_value=5,
        required=False,
        help_text=_('The level of discontent from 1 to 5'))
    description = forms.CharField(
        label='',
        max_length=300,
        required=True,
        widget=forms.Textarea(attrs={'placeholder': _('The reason of the grievance')}))

    def clean_plate(self):
        plate = self.cleaned_data['plate'].lower()
        plate = clean_p(plate)
        plate = map_words(plate)
        plate, country = validate_plate(plate)
        if not plate:
            raise forms.ValidationError(_('Try to put another plate. Example: A324BK23rus'))
        plate, __ = Plate.objects.get_or_create(name=plate, country=country)
        return plate

    class Meta:
        model = Grievance
        fields = ('plate', 'level', 'description')
