from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime

def current_date():
    return datetime.date.today()

def current_time():
    return str(timezone.now().time())[0:5]

# Create your models here.
class Cafeteria(models.Model):

    c_date = models.DateField(null=True, blank=False, verbose_name='Date', default=current_date)
    c_time = models.CharField(max_length=100, null=True, blank=False, verbose_name='Time (24 hr.)', default=current_time)
    c_coordinator = models.CharField(max_length=100, null=True, blank=True, verbose_name='Staff Pool Coordinator')
    c_main_doors = models.CharField(max_length=100, null=True, blank=True, verbose_name='Main Doors')
    c_south_patio_doors = models.CharField(max_length=100, null=True, blank=True, verbose_name='South Patio Doors')
    c_north_patio_doors_1 = models.CharField(max_length=100, null=True, blank=True, verbose_name='North Patio Doors 1')
    c_north_patio_doors_2 = models.CharField(max_length=100, null=True, blank=True, verbose_name='North Patio Doors 2')
    c_monitor = models.CharField(max_length=100, null=True, blank=True, verbose_name='Telephone Monitor')
    c_directors = models.CharField(max_length=100, null=True, blank=True, verbose_name='Patient/Visitor Director(s)')
    c_runners = models.CharField(max_length=100, null=True, blank=True, verbose_name='Command Centre Runner(s)')
    c_num_staff = models.CharField(max_length=100, null=True, blank=True, verbose_name='Number of Staff Present')
    c_explain = models.NullBooleanField(verbose_name='Explained to Participants')
    c_mock = models.NullBooleanField(verbose_name='Mock')

    class Meta:
        verbose_name_plural = 'Cafeteria'
        verbose_name = 'Cafeteria'

    def __str__(self):
        if self.c_coordinator == '' or self.c_coordinator is None :
            str_value = 'Undeclared Coordinator'
        else:
            str_value = self.c_coordinator

        return ', '.join([str(self.c_date), str_value])

    # def get_absolute_url(self):
    #     """Returns the url to access a detail record for this location."""
    #     return reverse('cafeteria_detail', args=[str(self.id)])


class East_Lobby(models.Model):
    e_date = models.DateField(null=True, blank=True, verbose_name='Date', default=current_date)
    e_time = models.CharField(max_length=100, null=True, blank=False, verbose_name='Time (24 hr.)', default=current_time)
    e_coordinator = models.CharField(max_length=100, null=True, blank=True, verbose_name='Staff Pool Coordinator')
    e_main_doors = models.CharField(max_length=100, null=True, blank=True, verbose_name='Main Doors')
    e_lab_entrance = models.CharField(max_length=100, null=True, blank=True, verbose_name='Lab Entrance')
    e_ed_entrance = models.CharField(max_length=100, null=True, blank=True, verbose_name='ED Entrance')
    e_monitor = models.CharField(max_length=100, null=True, blank=True, verbose_name='Telephone Monitor')
    e_directors = models.CharField(max_length=100, null=True, blank=True, verbose_name='Patient/Visitor Director(s)')
    e_runners = models.CharField(max_length=100, null=True, blank=True, verbose_name='Command Centre Runner(s)')
    e_num_staff = models.CharField(max_length=100, null=True, blank=True, verbose_name='Number of Staff Present')
    e_explain = models.NullBooleanField(verbose_name='Explained to Participants')
    e_mock = models.NullBooleanField(verbose_name='Mock')

    class Meta:
        verbose_name_plural = 'East Lobby'
        verbose_name = 'East Lobby'

    def __str__(self):
        if self.e_coordinator == '' or self.e_coordinator is None:
            str_value = 'Undeclared Coordinator'
        else:
            str_value = self.e_coordinator

        return ', '.join([str(self.e_date), str_value])

    # def get_absolute_url(self):
    #     """Returns the url to access a detail record for this location."""
    #     return reverse('east_lobby_detail', args=[str(self.id)])


class Town_Centre(models.Model):
    t_date = models.DateField(null=True, blank=True, verbose_name='Date', default=current_date)
    t_time = models.CharField(max_length=100, null=True, blank=False, verbose_name='Time (24 hr.)', default=current_time)
    t_coordinator = models.CharField(max_length=100, null=True, blank=True, verbose_name='Staff Pool Coordinator')
    t_horticultural = models.CharField(max_length=100, null=True, blank=True, verbose_name='Horticultural Entrance')
    t_town_centre_main_street = models.CharField(max_length=100, null=True, blank=True, verbose_name='Town Centre/Main Street')
    t_monitor = models.CharField(max_length=100, null=True, blank=True, verbose_name='Telephone Monitor')
    t_directors = models.CharField(max_length=100, null=True, blank=True, verbose_name='Patient/Visitor Director(s)')
    t_runners = models.CharField(max_length=100, null=True, blank=True, verbose_name='Command Centre Runner(s)')
    t_num_staff = models.CharField(max_length=100, null=True, blank=True, verbose_name='Number of Staff Present')
    t_explain = models.NullBooleanField(verbose_name='Explained to Participants')
    t_mock = models.NullBooleanField(verbose_name='Mock')

    class Meta:
        verbose_name_plural = 'Town Centre'
        verbose_name = 'Town Centre'

    def __str__(self):
        if self.t_coordinator == '' or self.t_coordinator is None:
            str_value = 'Undeclared Coordinator'
        else:
            str_value = self.t_coordinator

        return ', '.join([str(self.t_date), str_value])

    # def get_absolute_url(self):
    #     """Returns the url to access a detail record for this location."""
    #     return reverse('town_centre_detail', args=[str(self.id)])


class IncidentCommander(models.Model):
    i_date = models.DateField(null=True, blank=True, verbose_name='Date', default=current_date)
    i_time = models.CharField(max_length=100, null=True, blank=False, verbose_name='Time (24 hr.)', default=current_time)
    i_commander = models.CharField(max_length=100, null=True, blank=True, verbose_name='Incident Commander')
    i_num_staff_c = models.CharField(max_length=100, null=True, blank=True, verbose_name='Number of Staff at Cafeteria')
    i_num_staff_e = models.CharField(max_length=100, null=True, blank=True, verbose_name='Number of Staff at East Lobby')
    i_num_staff_t = models.CharField(max_length=100, null=True, blank=True, verbose_name='Number of Staff at Town Centre')
    i_captain = models.CharField(max_length=100, null=True, blank=True, verbose_name='Area Captain')
    i_signal_silence_time = models.CharField(max_length=100, null=True, blank=True, verbose_name='Time (24 hr.) of Signal Silence')
    i_all_clear_time = models.CharField(max_length=100, null=True, blank=True, verbose_name='Time (24 hr.) of All Clear')
    i_location_of_evacuation = models.CharField(max_length=100, null=True, blank=True, verbose_name='Location of Evacuation')
    i_area_of_refuge = models.CharField(max_length=100, null=True, blank=True, verbose_name='Area of Refuge')
    i_signed_fire_documentation = models.NullBooleanField(verbose_name='Signed Fire Department Documentation')
    i_mock = models.NullBooleanField(verbose_name='Mock')

    class Meta:
        verbose_name_plural = 'Incident Command'
        verbose_name = 'Incident Command'

    def __str__(self):
        if self.i_commander == '' or self.i_commander is None:
            str_value = 'Undeclared Commander'
        else:
            str_value = self.i_commander

        return ', '.join([str(self.i_date), str_value])


class CodeBlue(models.Model):
    blue_date = models.DateField(verbose_name='Date', default=current_date) # null and blank (required in forms) are False by default...
    blue_time = models.CharField(max_length=100, verbose_name='Time (24hr.)', default=current_time)
    blue_what_went_well = models.TextField(null=True, blank=True, verbose_name='What Went Well')
    blue_what_did_not_go_well = models.TextField(null=True, blank=True, verbose_name='What Didn\'t Go Well')
    blue_system_issues = models.TextField(null=True, blank=True, verbose_name='System Issues')
    blue_what_was_learned = models.TextField(null=True, blank=True, verbose_name='What Was Learned/Recommendations/Goals')
    blue_who_will_follow_up = models.TextField(null=True, blank=True, verbose_name='Who Will Follow Up/Communicate')
    blue_mock = models.NullBooleanField(verbose_name='Mock')

    class Meta:
        verbose_name_plural = 'Code Blue'
        verbose_name = 'Code Blue'

    def __str__(self):
        return 'Code Blue: ' + str(self.blue_date)


class CodePink(models.Model):
    pink_date = models.DateField(verbose_name='Date', default=current_date) # null and blank (required in forms) are False by default...
    pink_time = models.CharField(max_length=100, verbose_name='Time (24hr.)', default=current_time)
    pink_what_went_well = models.TextField(null=True, blank=True, verbose_name='What Went Well')
    pink_what_did_not_go_well = models.TextField(null=True, blank=True, verbose_name='What Didn\'t Go Well')
    pink_system_issues = models.TextField(null=True, blank=True, verbose_name='System Issues')
    pink_what_was_learned = models.TextField(null=True, blank=True, verbose_name='What Was Learned/Recommendations/Goals')
    pink_who_will_follow_up = models.TextField(null=True, blank=True, verbose_name='Who Will Follow Up/Communicate')
    pink_mock = models.NullBooleanField(verbose_name='Mock')

    class Meta:
        verbose_name_plural = 'Code Pink'
        verbose_name = 'Code Pink'

    def __str__(self):
        return 'Code Pink: ' + str(self.pink_date)


# class Commands(models.Model):
#     command_signal_silence = models.CharField(max_length = 100, verbose_name = 'Time of Signal Silence')
#     command_all_clear = models.

class CodeStatuses(models.Model):
    code_timestamp = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Time of Status Change')#, default=timezone.now()
    code_red_status = models.CharField(max_length=100, null=True, blank=True, verbose_name='Code Red Status', default='Normal')
    status_setter = models.CharField(max_length=100, null=True, blank=True, verbose_name='Status Setter')
    from_location = models.CharField(max_length=100, null=True, blank=True, verbose_name='From')
    to_location = models.CharField(max_length=100, null=True, blank=True, verbose_name='To')

    class Meta:
        verbose_name_plural = 'Code Red Status'
        verbose_name = 'Code Red Status'

    def __str__(self):

        if self.status_setter is not None and self.status_setter != '':
            status_setter = self.status_setter
            status_setter = ', ' + status_setter
        else:
            status_setter = ''

        if self.from_location is not None and self.from_location != '':
            from_location = self.from_location
            from_location = ', ' + from_location
        else:
            from_location = ''

        if self.to_location is not None and self.to_location != '':
            to_location = self.to_location
            to_location = ', ' + to_location
        else:
            to_location = ''

        return self.code_red_status + status_setter + from_location + to_location
