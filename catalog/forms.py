import datetime

from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from catalog.models import Cafeteria, East_Lobby, Town_Centre

class CafeteriaForm(forms.Form):
    c_date = forms.DateField(label='Date:', disabled=True, initial=timezone.now().date(), widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                 'placeholder': 'Date (yyyy-mm-dd)...'}))

    # c_time = forms.TimeField(required=True, label='Time (24 hr.)', widget=forms.widgets.TimeInput(attrs={'class': 'time-pick'}), input_formats=['%H:%M', '%I:%M%p', '%I:%M %p'])

    c_time = forms.CharField(required=False, label='Time (24 hr.)', disabled=True, initial=str(datetime.datetime.now().time())[0:5], widget=forms.TimeInput(attrs={'class': 'form-control form-control-sm',
                                                                                                  'placeholder': 'Time...'}))

    c_coordinator = forms.CharField(required=False, label='Staff Pool Coordinator', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                  'placeholder': 'Name...'}))

    c_main_doors = forms.CharField(required=False, label='Main Doors', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                     'placeholder': 'Name...'}))

    c_south_patio_doors = forms.CharField(required=False, label='South Patio Doors', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                   'placeholder': 'Name...'}))

    c_north_patio_doors_1 = forms.CharField(required=False, label='North Patio Doors (1)', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                         'placeholder': 'Name...'}))

    c_north_patio_doors_2 = forms.CharField(required=False, label='North Patio Doors (2)', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                         'placeholder': 'Name...'}))

    c_monitor = forms.CharField(required=False, label='Telephone Monitor', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                         'placeholder': 'Name...'}))

    c_directors = forms.CharField(required=False, label='Patient/Visitor Director(s)', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                     'placeholder': 'Name(s)...'}))

    c_runners = forms.CharField(required=False, label='Command Centre Runner(s)', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                'placeholder': 'Name(s)...'}))

    c_num_staff = forms.CharField(required=False, label='Number of Staff Present', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                 'placeholder': 'Count...'}))

    c_explain = forms.NullBooleanField(label=mark_safe('Staff Pool participants told</br>to listen for new instructions</br> and check back in with the</br>Pool Coordinator on return'))#, widget=forms.CheckboxInput(attrs={'class': 'form-check-lg'}))

    def clean_c_date(self):
        data = self.cleaned_data['c_date']
        return data

    def clean_c_time(self):
        data = self.cleaned_data['c_time']
        return data

    def clean_c_coordinator(self):
        data = self.cleaned_data['c_coordinator']
        return data

    def clean_c_main_doors(self):
        data = self.cleaned_data['c_main_doors']
        return data

    def clean_c_main_doors(self):
        data = self.cleaned_data['c_main_doors']
        return data

    def clean_c_south_patio_doors(self):
        data = self.cleaned_data['c_south_patio_doors']
        return data

    def clean_c_north_patio_doors_1(self):
        data = self.cleaned_data['c_north_patio_doors_1']
        return data

    def clean_c_north_patio_doors_2(self):
        data = self.cleaned_data['c_north_patio_doors_2']
        return data

    def clean_c_monitor(self):
        data = self.cleaned_data['c_monitor']
        return data

    def clean_c_directors(self):
        data = self.cleaned_data['c_directors']
        return data

    def clean_c_runners(self):
        data = self.cleaned_data['c_runners']
        return data

    def clean_c_num_staff(self):
        data = self.cleaned_data['c_num_staff']
        return data

    def clean_c_explain(self):
        data = self.cleaned_data['c_explain']
        return data


class East_LobbyForm(forms.Form):
    e_date = forms.DateField(label='Date:', disabled=True, initial=timezone.now().date(), widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                 'placeholder': 'Date (yyyy-mm-dd)...'}))

    e_time = forms.CharField(required=False, label='Time (24 hr.)', widget=forms.TimeInput(attrs={'class': 'form-control form-control-sm',
                                                                                                  'placeholder': 'Time...'}))

    e_coordinator = forms.CharField(required=False, label='Staff Pool Coordinator', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                         'placeholder': 'Name...'}))

    e_main_doors = forms.CharField(required=False, label='Main Doors', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                         'placeholder': 'Name...'}))

    e_lab_entrance = forms.CharField(required=False, label='Lab Entrance', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                         'placeholder': 'Name...'}))

    e_ed_entrance = forms.CharField(required=False, label='ED Entrance', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                         'placeholder': 'Name...'}))

    e_monitor = forms.CharField(required=False, label='Telephone Monitor', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                         'placeholder': 'Name...'}))

    e_directors = forms.CharField(required=False, label='Patient/Visitor Director(s)', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                         'placeholder': 'Name(s)...'}))

    e_runners = forms.CharField(required=False, label='Command Centre Runner(s)', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                         'placeholder': 'Name(s)...'}))

    e_num_staff = forms.CharField(required=False, label='Number of Staff Present', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                 'placeholder': 'Count...'}))

    e_explain = forms.NullBooleanField(label=mark_safe('Staff Pool participants told</br>to listen for new instructions</br> and check back in with the</br>Pool Coordinator on return'))

    def clean_e_date(self):
        data = self.cleaned_data['e_date']
        return data

    def clean_e_time(self):
        data = self.cleaned_data['e_time']
        return data

    def clean_e_coordinator(self):
        data = self.cleaned_data['e_coordinator']
        return data

    def clean_e_main_doors(self):
        data = self.cleaned_data['e_main_doors']
        return data

    def clean_e_lab_entrance(self):
        data = self.cleaned_data['e_lab_entrance']
        return data

    def clean_e_ed_entrance(self):
        data = self.cleaned_data['e_ed_entrance']
        return data

    def clean_e_monitor(self):
        data = self.cleaned_data['e_monitor']
        return data

    def clean_e_directors(self):
        data = self.cleaned_data['e_directors']
        return data

    def clean_e_runners(self):
        data = self.cleaned_data['e_runners']
        return data

    def clean_e_num_staff(self):
        data = self.cleaned_data['e_num_staff']
        return data

    def clean_e_explain(self):
        data = self.cleaned_data['e_explain']
        return data


class Town_CentreForm(forms.Form):
    t_date = forms.DateField(label='Date:', disabled=True, initial=timezone.now().date(), widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                 'placeholder': 'Date (yyyy-mm-dd)...'}))

    t_time = forms.CharField(required=False, label='Time (24 hr.)', widget=forms.TimeInput(attrs={'class': 'form-control form-control-sm',
                                                                                                  'placeholder': 'Time...'}))

    t_coordinator = forms.CharField(required=False, label='Staff Pool Coordinator', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                         'placeholder': 'Name...'}))

    t_horticultural = forms.CharField(required=False, label='Horticultural Entrance', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                         'placeholder': 'Name...'}))

    t_town_centre_main_street = forms.CharField(required=False, label='Town Centre/Main Street', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                         'placeholder': 'Name...'}))

    t_monitor = forms.CharField(required=False, label='Telephone Monitor', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                         'placeholder': 'Name...'}))

    t_directors = forms.CharField(required=False, label='Patient/Visitor Director(s)', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                         'placeholder': 'Name(s)...'}))

    t_runners = forms.CharField(required=False, label='Command Centre Runner(s)', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                         'placeholder': 'Name(s)...'}))

    t_num_staff = forms.CharField(required=False, label='Number of Staff Present', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                 'placeholder': 'Count...'}))

    t_explain = forms.NullBooleanField(label=mark_safe('Staff Pool participants told</br>to listen for new instructions</br> and check back in with the</br>Pool Coordinator on return'))

    def clean_t_date(self):
        data = self.cleaned_data['t_date']
        return data

    def clean_t_time(self):
        data = self.cleaned_data['t_time']
        return data

    def clean_t_coordinator(self):
        data = self.cleaned_data['t_coordinator']
        return data

    def clean_t_horticultural(self):
        data = self.cleaned_data['t_horticultural']
        return data

    def clean_t_town_centre_main_street(self):
        data = self.cleaned_data['t_town_centre_main_street']
        return data

    def clean_t_monitor(self):
        data = self.cleaned_data['t_monitor']
        return data

    def clean_t_directors(self):
        data = self.cleaned_data['t_directors']
        return data

    def clean_t_runners(self):
        data = self.cleaned_data['t_runners']
        return data

    def clean_t_num_staff(self):
        data = self.cleaned_data['t_num_staff']
        return data

    def clean_t_explain(self):
        data = self.cleaned_data['t_explain']
        return data
