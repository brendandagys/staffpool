import datetime

from django import forms
# from django.forms import ModelForm
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from catalog.models import Cafeteria, East_Lobby, Town_Centre, IncidentCommander, CodeBlue, CodePink

class CafeteriaForm(forms.Form):
    c_date = forms.DateField(label='Date:', disabled=True, initial=lambda: datetime.date.today(), widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                 'placeholder': 'Date (yyyy-mm-dd)...'}))

    c_time = forms.CharField(required=False, label='Time (24 hr.)', disabled=True, initial=lambda: str(timezone.now().time())[0:5], widget=forms.TimeInput(attrs={'class': 'form-control form-control-sm',
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

    c_mock = forms.NullBooleanField(label='Mock Drill')


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

    def clean_c_mock(self):
        data = self.cleaned_data['c_mock']
        return data


class East_LobbyForm(forms.Form):
    e_date = forms.DateField(label='Date:', disabled=True, initial=lambda: datetime.date.today(), widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                 'placeholder': 'Date (yyyy-mm-dd)...'}))

    e_time = forms.CharField(required=False, label='Time (24 hr.)', disabled=True, initial=lambda: str(timezone.now().time())[0:5], widget=forms.TimeInput(attrs={'class': 'form-control form-control-sm',
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

    e_mock = forms.NullBooleanField(label='Mock Drill')


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

    def clean_e_mock(self):
        data = self.cleaned_data['e_mock']
        return data


class Town_CentreForm(forms.Form):
    t_date = forms.DateField(label='Date:', disabled=True, initial=lambda: datetime.date.today(), widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                                                                                 'placeholder': 'Date (yyyy-mm-dd)...'}))

    t_time = forms.CharField(required=False, label='Time (24 hr.)', disabled=True, initial=lambda: str(timezone.now().time())[0:5], widget=forms.TimeInput(attrs={'class': 'form-control form-control-sm',
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

    t_mock = forms.NullBooleanField(label='Mock Drill')


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

    def clean_t_mock(self):
        data = self.cleaned_data['t_mock']
        return data


class IncidentCommanderForm(forms.Form):
    i_date = forms.DateField(label='Date:', disabled=True, initial=lambda: datetime.date.today(),
                widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Date (yyyy-mm-dd)...'}))

    i_time = forms.CharField(required=False, label='Time (24 hr.)', disabled=True, initial=lambda: str(timezone.now().time())[0:5],
                widget=forms.TimeInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Time...'}))

    i_commander = forms.CharField(required=False, label='Incident Commander',
                        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Name...'}))

    i_num_staff_c = forms.CharField(required=False, label='# of Staff at Cafeteria',
            widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Count...'}))

    i_num_staff_e = forms.CharField(required=False, label='# of Staff at East Lobby',
            widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Count...'}))

    i_num_staff_t = forms.CharField(required=False, label='# of Staff at Town Centre',
            widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Count...'}))

    i_captain = forms.CharField(required=False, label='Area Captain',
            widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Name...'}))

    i_signal_silence_time = forms.CharField(required=False, label='Time of Signal Silence',
            widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter a time...'}))

    i_all_clear_time = forms.CharField(required=False, label='Time of All Clear',
            widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter a time...'}))

    i_location_of_evacuation = forms.CharField(required=False, label='Location of Evacuation',
            widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter a location...'}))

    i_area_of_refuge = forms.CharField(required=False, label='Area of Refuge',
            widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter a location...'}))

    i_signed_fire_documentation = forms.NullBooleanField(label=mark_safe('Signed off on appropriate municipal fire department documentation'))

    i_mock = forms.NullBooleanField(label='Mock Drill')


    def clean_i_date(self):
        data = self.cleaned_data['i_date']
        return data

    def clean_i_time(self):
        data = self.cleaned_data['i_time']
        return data

    def clean_i_commander(self):
        data = self.cleaned_data['i_commander']
        return data

    def clean_i_num_staff_c(self):
        data = self.cleaned_data['i_num_staff_c']
        return data

    def clean_i_num_staff_e(self):
        data = self.cleaned_data['i_num_staff_e']
        return data

    def clean_i_num_staff_t(self):
        data = self.cleaned_data['i_num_staff_t']
        return data

    def clean_i_captain(self):
        data = self.cleaned_data['i_captain']
        return data

    def clean_i_signal_silence_time(self):
        data = self.cleaned_data['i_signal_silence_time']
        return data

    def clean_i_all_clear_time(self):
        data = self.cleaned_data['i_all_clear_time']
        return data

    def clean_i_location_of_evacuation(self):
        data = self.cleaned_data['i_location_of_evacuation']
        return data

    def clean_i_area_of_refuge(self):
        data = self.cleaned_data['i_area_of_refuge']
        return data

    def clean_i_signed_fire_documentation(self):
        data = self.cleaned_data['i_signed_fire_documentation']
        return data

    def clean_i_mock(self):
        data = self.cleaned_data['i_mock']
        return data


class Code_BlueForm(forms.Form):
    blue_date = forms.DateField(label='Date:', disabled=True, initial=lambda: datetime.date.today(),
                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date (yyyy-mm-dd)...'}))

    blue_time = forms.CharField(required=False, label='Time (24 hr.)', disabled=True, initial=lambda: str(timezone.now().time())[0:5],
                    widget=forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Time...'}))

    blue_what_went_well = forms.CharField(required=False, label='What went well?',
                            widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '15', 'placeholder': 'Please answer here...'}))

    blue_what_did_not_go_well = forms.CharField(required=False, label='What didn\'t go well? What would we do differently next time?',
                                    widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '15', 'placeholder': 'Please answer here...'}))

    blue_system_issues = forms.CharField(required=False, label='Any system issues, such as equipment, processes, information flow?',
                            widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '15', 'placeholder': 'Please answer here...'}))

    blue_what_was_learned = forms.CharField(required=False, label='What was learned? Any recommendations or goals for next time?',
                                widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '15', 'placeholder': 'Please answer here...'}))

    blue_who_will_follow_up = forms.CharField(required=False, label='Who will follow up? How will we communicate back to the team?',
                                widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '15', 'placeholder': 'Please answer here...'}))

    blue_mock = forms.NullBooleanField(label='Mock Drill')


    def clean_blue_date(self):
        data = self.cleaned_data['blue_date']
        return data

    def clean_blue_time(self):
        data = self.cleaned_data['blue_time']
        return data

    def clean_blue_what_went_well(self):
        data = self.cleaned_data['blue_what_went_well']
        return data

    def clean_blue_what_did_not_go_well(self):
        data = self.cleaned_data['blue_what_did_not_go_well']
        return data

    def clean_blue_system_issues(self):
        data = self.cleaned_data['blue_system_issues']
        return data

    def clean_blue_what_was_learned(self):
        data = self.cleaned_data['blue_what_was_learned']
        return data

    def clean_blue_mock(self):
        data = self.cleaned_data['blue_mock']
        return data


class Code_PinkForm(forms.Form):
    pink_date = forms.DateField(label='Date:', disabled=True, initial=lambda: datetime.date.today(),
                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date (yyyy-mm-dd)...'}))

    pink_time = forms.CharField(required=False, label='Time (24 hr.)', disabled=True, initial=lambda: str(timezone.now().time())[0:5],
                    widget=forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Time...'}))

    pink_what_went_well = forms.CharField(required=False, label='What went well?',
                            widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '15', 'placeholder': 'Please answer here...'}))

    pink_what_did_not_go_well = forms.CharField(required=False, label='What didn\'t go well? What would we do differently next time?',
                                    widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '15', 'placeholder': 'Please answer here...'}))

    pink_system_issues = forms.CharField(required=False, label='Any system issues, such as equipment, processes, information flow?',
                            widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '15', 'placeholder': 'Please answer here...'}))

    pink_what_was_learned = forms.CharField(required=False, label='What was learned? Any recommendations or goals for next time?',
                                widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '15', 'placeholder': 'Please answer here...'}))

    pink_who_will_follow_up = forms.CharField(required=False, label='Who will follow up? How will we communicate back to the team?',
                                widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '15', 'placeholder': 'Please answer here...'}))

    pink_mock = forms.NullBooleanField(label='Mock Drill')


    def clean_pink_date(self):
        data = self.cleaned_data['pink_date']
        return data

    def clean_pink_time(self):
        data = self.cleaned_data['pink_time']
        return data

    def clean_pink_what_went_well(self):
        data = self.cleaned_data['pink_what_went_well']
        return data

    def clean_pink_what_did_not_go_well(self):
        data = self.cleaned_data['pink_what_did_not_go_well']
        return data

    def clean_pink_system_issues(self):
        data = self.cleaned_data['pink_system_issues']
        return data

    def clean_pink_what_was_learned(self):
        data = self.cleaned_data['pink_what_was_learned']
        return data

    def clean_pink_mock(self):
        data = self.cleaned_data['pink_mock']
        return data
