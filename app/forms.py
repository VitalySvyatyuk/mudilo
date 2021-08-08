from django import forms

from .models import Grievance, Plate
from .utils import clean_p, map_words, validate_plate


class GrievanceForm(forms.ModelForm):
    plate = forms.CharField(
        label='',
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Пример: A324BK23rus'}),
        help_text='Автомобильный номер')
    level = forms.IntegerField(
        label='',
        initial=3,
        min_value=1,
        max_value=5,
        required=False,
        help_text='Уровень возмущения от 1 до 5, где 5 - крайне возмущен!')
    description = forms.CharField(
        label='',
        max_length=2000,
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Описание ситуации'}))
    # image = forms.ImageField(
    #     label='',
    #     required=False,
    #     help_text='Прикрепить картинку (необязательное поле)'
    # )
    # email = forms.CharField(
    #     label='',
    #     max_length=100,
    #     required=False,
    #     widget=forms.TextInput(attrs={'placeholder': 'Email'}),
    #     help_text='Email, на который отправим результат (необязательное поле)')

    def clean_plate(self):
        plate = self.cleaned_data['plate'].lower()
        plate = clean_p(plate)
        plate = map_words(plate)
        plate, country = validate_plate(plate)
        if not plate:
            raise forms.ValidationError('Попробуйте ещё раз. Пример: A324BK23rus')
        plate, __ = Plate.objects.get_or_create(name=plate, country=country)
        return plate

    class Meta:
        model = Grievance
        fields = ('plate', 'level', 'description')
