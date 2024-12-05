from django import forms
from .models import Rezervacie,Timy, TypZapasu, HraciePlochy, Hraci, Zaujem
from bootstrap_datepicker_plus.widgets import DatePickerInput,TimePickerInput
#from bootstrap4.forms import ModelForm

AKTIVITA_CHOICES =(
    ("A", "Aktívny"),
    ("N", "Neaktívny"),
)

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Rezervacie
        fields = ['hracieplochy', 'typzapasu', 'tim', 'date',  'start_time', 'end_time']
        tim = forms.ModelMultipleChoiceField(queryset=Timy.objects.all())
        hracieplochy = forms.ModelMultipleChoiceField(queryset=HraciePlochy.objects.all())
        typzapasu = forms.ModelMultipleChoiceField(queryset=TypZapasu.objects.all())
#forms.ModelChoiceField(queryset=Timy.objects.all())
        widgets = {
            'date': DatePickerInput(options={"format": "DD.MM.YYYY"}),
            'start_time' : TimePickerInput(),
            'end_time' : TimePickerInput().start_of('start_time'),
        }
        # Prípadne ďalšie polia pre rezerváciu

class HraciForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HraciForm, self).__init__(*args, **kwargs)
#        self.fields['datum_narodenia'].disabled = True
    class Meta:
        model = Hraci
        fields = ['meno', 'priezvisko', 'aktivita', 'tim', 'datum_narodenia']
#        aktivita = forms.ModelMultipleChoiceField(queryset=Zaujem.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
        tim = forms.ModelMultipleChoiceField(queryset=Zaujem.objects.all())
        widgets = {
            'datum_narodenia': DatePickerInput(options={"format": "DD.MM.YYYY"}),
            'aktivita': forms.Select(choices = AKTIVITA_CHOICES, attrs={'class': 'form-control'}),
        }


class HraciFilterForm(forms.Form):
    filter_tim = forms.ModelChoiceField(queryset=Timy.objects.all())
    filter_aktivita = forms.ChoiceField(choices = AKTIVITA_CHOICES)

    def filter_hracis(self):
        tim = self.cleaned_data.get('tim')
        aktivita = self.cleaned_data.get('aktivita')
        hracis = Hraci.objects.all()

        if tim:
            hracis = hracis.filter(tim=tim)

        if aktivita:
            hracis = hracis.filter(aktivita=aktivita)

        return hracis