import datetime

import json
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

# Create your views here.
from catalog.models import Cafeteria, East_Lobby, Town_Centre, CodeStatuses
from catalog.forms import CafeteriaForm, East_LobbyForm, Town_CentreForm

@login_required
def cafeteria_form(request):
    '''View function for home page of site.'''

    num_events = Cafeteria.objects.all().count() # All is implied by default

    if request.method == 'POST' and 'c' in request.POST:

        if Cafeteria.objects.last() is None:
            cafeteria_instance = Cafeteria()

        else:

            if ((Cafeteria.objects.last().c_date == timezone.now().date()) and
               ((abs(int(Cafeteria.objects.last().c_time[0:2]) - int(str(datetime.datetime.now().time())[0:2])) == 0)) or
               ( (abs(int(Cafeteria.objects.last().c_time[0:2]) - int(str(datetime.datetime.now().time())[0:2])) == 1) and (int(Cafeteria.objects.last().c_time[3:5]) > int(str(datetime.datetime.now().time())[3:5])) )):

                cafeteria_instance = Cafeteria.objects.all().order_by('-id')[:1][0]

            else:
                cafeteria_instance = Cafeteria()

        # Create a form instance and populate it with data from the request (binding):
        form_c = CafeteriaForm(request.POST)
        # print(form_c.errors)

        # Check if the form is valid:
        if form_c.is_valid():

            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            cafeteria_instance.c_date = form_c.cleaned_data['c_date']
            cafeteria_instance.c_time = form_c.cleaned_data['c_time']#.strip()
            cafeteria_instance.c_coordinator = form_c.cleaned_data['c_coordinator'].strip()
            cafeteria_instance.c_main_doors = form_c.cleaned_data['c_main_doors'].strip()
            cafeteria_instance.c_south_patio_doors = form_c.cleaned_data['c_south_patio_doors'].strip()
            cafeteria_instance.c_north_patio_doors_1 = form_c.cleaned_data['c_north_patio_doors_1'].strip()
            cafeteria_instance.c_north_patio_doors_2 = form_c.cleaned_data['c_north_patio_doors_2'].strip()
            cafeteria_instance.c_monitor = form_c.cleaned_data['c_monitor'].strip()
            cafeteria_instance.c_directors = form_c.cleaned_data['c_directors'].strip()
            cafeteria_instance.c_runners = form_c.cleaned_data['c_runners'].strip()
            cafeteria_instance.c_num_staff = form_c.cleaned_data['c_num_staff'].strip()
            cafeteria_instance.c_explain = form_c.cleaned_data['c_explain']

            cafeteria_instance.save()

        # redirect to a new URL:
        return HttpResponseRedirect(reverse('LIVE') )

    # If this is a GET (or any other method) create the default form.
    else:

        try:
            if ((Cafeteria.objects.last().c_date == timezone.now().date()) and
               ((abs(int(Cafeteria.objects.last().c_time[0:2]) - int(str(datetime.datetime.now().time())[0:2])) == 0)) or
               ( (abs(int(Cafeteria.objects.last().c_time[0:2]) - int(str(datetime.datetime.now().time())[0:2])) == 1) and (int(Cafeteria.objects.last().c_time[3:5]) > int(str(datetime.datetime.now().time())[3:5])) )):

                c_time = Cafeteria.objects.last().c_time
                c_coordinator = Cafeteria.objects.last().c_coordinator # Will return None if no match
                c_main_doors = Cafeteria.objects.last().c_main_doors
                c_south_patio_doors = Cafeteria.objects.last().c_south_patio_doors
                c_north_patio_doors_1 = Cafeteria.objects.last().c_north_patio_doors_1
                c_north_patio_doors_2 = Cafeteria.objects.last().c_north_patio_doors_2
                c_monitor = Cafeteria.objects.last().c_monitor
                c_directors = Cafeteria.objects.last().c_directors
                c_runners = Cafeteria.objects.last().c_runners
                c_num_staff = Cafeteria.objects.last().c_num_staff
                c_explain = Cafeteria.objects.last().c_explain

            else:
                c_time = str(datetime.datetime.now().time())[0:5]
                c_coordinator = ''
                c_main_doors = ''
                c_south_patio_doors = ''
                c_north_patio_doors_1 = ''
                c_north_patio_doors_2 = ''
                c_monitor = ''
                c_directors = ''
                c_runners = ''
                c_num_staff = ''
                c_explain = ''

        except:
            c_time = str(datetime.datetime.now().time())[0:5]
            c_coordinator = ''
            c_main_doors = ''
            c_south_patio_doors = ''
            c_north_patio_doors_1 = ''
            c_north_patio_doors_2 = ''
            c_monitor = ''
            c_directors = ''
            c_runners = ''
            c_num_staff = ''
            c_explain = ''

        form_c = CafeteriaForm(initial={'c_date': timezone.now().date(),
                                        'c_time': c_time,
                                        'c_coordinator': c_coordinator,
                                        'c_main_doors': c_main_doors,
                                        'c_south_patio_doors': c_south_patio_doors,
                                        'c_north_patio_doors_1': c_north_patio_doors_1,
                                        'c_north_patio_doors_2': c_north_patio_doors_2,
                                        'c_monitor': c_monitor,
                                        'c_directors': c_directors,
                                        'c_runners': c_runners,
                                        'c_num_staff': c_num_staff,
                                        'c_explain': c_explain
                                        })

    context = { 'num_events': num_events,
                'form_c': form_c, }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'cafeteria_form.html', context=context)

# ==================================================================================================

@login_required
def east_lobby_form(request):
    '''View function for home page of site.'''

    num_events = East_Lobby.objects.all().count() # All is implied by default

    if request.method == 'POST' and 'e' in request.POST:

        if East_Lobby.objects.last() is None:
            east_lobby_instance = East_Lobby()

        else:

            if ((East_Lobby.objects.last().e_date == timezone.now().date()) and
               ((abs(int(East_Lobby.objects.last().e_time[0:2]) - int(str(datetime.datetime.now().time())[0:2])) == 0)) or
               ( (abs(int(East_Lobby.objects.last().e_time[0:2]) - int(str(datetime.datetime.now().time())[0:2])) == 1) and (int(East_Lobby.objects.last().e_time[3:5]) > int(str(datetime.datetime.now().time())[3:5])) )):

                east_lobby_instance = East_Lobby.objects.all().order_by('-id')[:1][0]

            else:
                east_lobby_instance = East_Lobby()

        # Create a form instance and populate it with data from the request (binding):
        form_e = East_LobbyForm(request.POST)
        # print(form_c.errors)

        # Check if the form is valid:
        if form_e.is_valid():

            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            east_lobby_instance.e_date = form_e.cleaned_data['e_date']
            east_lobby_instance.e_time = form_e.cleaned_data['e_time']#.strip()
            east_lobby_instance.e_coordinator = form_e.cleaned_data['e_coordinator'].strip()
            east_lobby_instance.e_main_doors = form_e.cleaned_data['e_main_doors'].strip()
            east_lobby_instance.e_lab_entrance = form_e.cleaned_data['e_lab_entrance'].strip()
            east_lobby_instance.e_ed_entrance = form_e.cleaned_data['e_ed_entrance'].strip()
            east_lobby_instance.e_monitor = form_e.cleaned_data['e_monitor'].strip()
            east_lobby_instance.e_directors = form_e.cleaned_data['e_directors'].strip()
            east_lobby_instance.e_runners = form_e.cleaned_data['e_runners'].strip()
            east_lobby_instance.e_num_staff = form_e.cleaned_data['e_num_staff'].strip()
            east_lobby_instance.e_explain = form_e.cleaned_data['e_explain']

            east_lobby_instance.save()

        # redirect to a new URL:
        return HttpResponseRedirect(reverse('LIVE') )

    # If this is a GET (or any other method) create the default form.
    else:

        try:
            if ((East_Lobby.objects.last().e_date == timezone.now().date()) and
               ((abs(int(East_Lobby.objects.last().e_time[0:2]) - int(str(datetime.datetime.now().time())[0:2])) == 0)) or
               ( (abs(int(East_Lobby.objects.last().e_time[0:2]) - int(str(datetime.datetime.now().time())[0:2])) == 1) and (int(East_Lobby.objects.last().e_time[3:5]) > int(str(datetime.datetime.now().time())[3:5])) )):

                e_time = East_Lobby.objects.last().e_time
                e_coordinator = East_Lobby.objects.last().e_coordinator # Will return None if no match
                e_main_doors = East_Lobby.objects.last().e_main_doors
                e_lab_entrance = East_Lobby.objects.last().e_lab_entrance
                e_ed_entrance = East_Lobby.objects.last().e_ed_entrance
                e_monitor = East_Lobby.objects.last().e_monitor
                e_directors = East_Lobby.objects.last().e_directors
                e_runners = East_Lobby.objects.last().e_runners
                e_num_staff = East_Lobby.objects.last().e_num_staff
                e_explain = East_Lobby.objects.last().e_explain

            else:
                e_time = str(datetime.datetime.now().time())[0:5]
                e_coordinator = ''
                e_main_doors = ''
                e_lab_entrance = ''
                e_ed_entrance = ''
                e_monitor = ''
                e_directors = ''
                e_runners = ''
                e_num_staff = ''
                e_explain = ''

        except:
            e_time = str(datetime.datetime.now().time())[0:5]
            e_coordinator = ''
            e_main_doors = ''
            e_lab_entrance = ''
            e_ed_entrance = ''
            e_monitor = ''
            e_directors = ''
            e_runners = ''
            e_num_staff = ''
            e_explain = ''

        form_e = East_LobbyForm(initial={'e_date': timezone.now().date(),
                                        'e_time': e_time,
                                        'e_coordinator': e_coordinator,
                                        'e_main_doors': e_main_doors,
                                        'e_lab_entrance': e_lab_entrance,
                                        'e_ed_entrance': e_ed_entrance,
                                        'e_monitor': e_monitor,
                                        'e_directors': e_directors,
                                        'e_runners': e_runners,
                                        'e_num_staff': e_num_staff,
                                        'e_explain': e_explain
                                        })

    context = { 'num_events': num_events,
                'form_e': form_e, }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'east_lobby_form.html', context=context)

# ==================================================================================================

@login_required
def town_centre_form(request):
    '''View function for home page of site.'''

    num_events = Town_Centre.objects.all().count() # All is implied by default

    if request.method == 'POST' and 't' in request.POST:

        if Town_Centre.objects.last() is None:
            town_centre_instance = Town_Centre()

        else:

            if ((Town_Centre.objects.last().t_date == timezone.now().date()) and
               ((abs(int(Town_Centre.objects.last().t_time[0:2]) - int(str(datetime.datetime.now().time())[0:2])) == 0)) or
               ( (abs(int(Town_Centre.objects.last().t_time[0:2]) - int(str(datetime.datetime.now().time())[0:2])) == 1) and (int(Town_Centre.objects.last().t_time[3:5]) > int(str(datetime.datetime.now().time())[3:5])) )):

                town_centre_instance = Town_Centre.objects.all().order_by('-id')[:1][0]

            else:
                town_centre_instance = Town_Centre()

        # Create a form instance and populate it with data from the request (binding):
        form_t = Town_CentreForm(request.POST)
        # print(form_c.errors)

        # Check if the form is valid:
        if form_t.is_valid():

            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            town_centre_instance.t_date = form_t.cleaned_data['t_date']
            town_centre_instance.t_time = form_t.cleaned_data['t_time']#.strip()
            town_centre_instance.t_coordinator = form_t.cleaned_data['t_coordinator'].strip()
            town_centre_instance.t_horticultural = form_t.cleaned_data['t_horticultural'].strip()
            town_centre_instance.t_town_centre_main_street = form_t.cleaned_data['t_town_centre_main_street'].strip()
            town_centre_instance.t_monitor = form_t.cleaned_data['t_monitor'].strip()
            town_centre_instance.t_directors = form_t.cleaned_data['t_directors'].strip()
            town_centre_instance.t_runners = form_t.cleaned_data['t_runners'].strip()
            town_centre_instance.t_num_staff = form_t.cleaned_data['t_num_staff'].strip()
            town_centre_instance.t_explain = form_t.cleaned_data['t_explain']

            town_centre_instance.save()

        # redirect to a new URL:
        return HttpResponseRedirect(reverse('LIVE') )

    # If this is a GET (or any other method) create the default form.
    else:

        try:

            if ((Town_Centre.objects.last().t_date == timezone.now().date()) and
               ((abs(int(Town_Centre.objects.last().t_time[0:2]) - int(str(datetime.datetime.now().time())[0:2])) == 0)) or
               ( (abs(int(Town_Centre.objects.last().t_time[0:2]) - int(str(datetime.datetime.now().time())[0:2])) == 1) and (int(Town_Centre.objects.last().t_time[3:5]) > int(str(datetime.datetime.now().time())[3:5])) )):

                t_time = Town_Centre.objects.last().t_time
                t_coordinator = Town_Centre.objects.last().t_coordinator # Will return None if no match
                t_horticultural = Town_Centre.objects.last().t_horticultural
                t_town_centre_main_street = Town_Centre.objects.last().t_town_centre_main_street
                t_monitor = Town_Centre.objects.last().t_monitor
                t_directors = Town_Centre.objects.last().t_directors
                t_runners = Town_Centre.objects.last().t_runners
                t_num_staff = Town_Centre.objects.last().t_num_staff
                t_explain = Town_Centre.objects.last().t_explain

            else:
                t_time = str(datetime.datetime.now().time())[0:5]
                t_coordinator = ''
                t_horticultural = ''
                t_town_centre_main_street = ''
                t_monitor = ''
                t_directors = ''
                t_runners = ''
                t_num_staff = ''
                t_explain = ''

        except:
            t_time = str(datetime.datetime.now().time())[0:5]
            t_coordinator = ''
            t_horticultural = ''
            t_town_centre_main_street = ''
            t_monitor = ''
            t_directors = ''
            t_runners = ''
            t_num_staff = ''
            t_explain = ''

        form_t = Town_CentreForm(initial={'t_date': timezone.now().date(),
                                        't_time': t_time,
                                        't_coordinator': t_coordinator,
                                        't_horticultural': t_horticultural,
                                        't_town_centre_main_street': t_town_centre_main_street,
                                        't_monitor': t_monitor,
                                        't_directors': t_directors,
                                        't_runners': t_runners,
                                        't_num_staff': t_num_staff,
                                        't_explain': t_explain
                                        })

    context = { 'num_events': num_events,
                'form_t': form_t, }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'town_centre_form.html', context=context)

# ==================================================================================================

class LocationListView(LoginRequiredMixin, generic.ListView):
    model = Cafeteria
    context_object_name = 'location_list'
    # queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    template_name = 'location_list.html' # Specify your own template name/location

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(LocationListView, self).get_context_data(**kwargs)



        if ((Cafeteria.objects.last().c_date == timezone.now().date()) and
           ((abs(int(Cafeteria.objects.last().c_time[0:2]) - int(str(datetime.datetime.now().time())[0:2])) == 0)) or
           ( (abs(int(Cafeteria.objects.last().c_time[0:2]) - int(str(datetime.datetime.now().time())[0:2])) == 1) and (int(Cafeteria.objects.last().c_time[3:5]) > int(str(datetime.datetime.now().time())[3:5])) )):

            temporary_instance = Cafeteria.objects.last() # last() doesn't return a Queryset!!!

        else:
            temporary_instance = None


        try:

            if (temporary_instance.c_time is None):
                temporary_instance.c_time = ''

            if (temporary_instance.c_coordinator is None):
                temporary_instance.c_coordinator = ''

            if (temporary_instance.c_main_doors is None):
                temporary_instance.c_main_doors = ''

            if (temporary_instance.c_south_patio_doors is None):
                temporary_instance.c_south_patio_doors = ''

            if (temporary_instance.c_north_patio_doors_1 is None):
                temporary_instance.c_north_patio_doors_1 = ''

            if (temporary_instance.c_north_patio_doors_2 is None):
                temporary_instance.c_north_patio_doors_2 = ''

            if (temporary_instance.c_monitor is None):
                temporary_instance.c_monitor = ''

            if (temporary_instance.c_directors is None):
                temporary_instance.c_directors = ''

            if (temporary_instance.c_runners is None):
                temporary_instance.c_runners = ''

            if (temporary_instance.c_num_staff is None):
                temporary_instance.c_num_staff = ''

            temporary_instance.save()

            context['cafeteria'] = Cafeteria.objects.all().order_by('-id')[:1]

        except:
            pass

        try:
            if context['cafeteria'][0].c_explain is True:
                context['c_explainval'] = 'Yes'
            else:
                context['c_explainval'] = 'No'
        except:
            pass


        if ((East_Lobby.objects.last().e_date == timezone.now().date()) and
           ((abs(int(East_Lobby.objects.last().e_time[0:2]) - int(str(datetime.datetime.now().time())[0:2])) == 0)) or
           ( (abs(int(East_Lobby.objects.last().e_time[0:2]) - int(str(datetime.datetime.now().time())[0:2])) == 1) and (int(East_Lobby.objects.last().e_time[3:5]) > int(str(datetime.datetime.now().time())[3:5])) )):

            temporary_instance_e = East_Lobby.objects.last() # last() doesn't return a Queryset!!!

        else:
            temporary_instance_e = None

        try:

            if (temporary_instance_e.e_time is None):
                temporary_instance_e.e_time = ''

            if (temporary_instance_e.e_coordinator is None):
                temporary_instance_e.e_coordinator = ''

            if (temporary_instance_e.e_main_doors is None):
                temporary_instance_e.e_main_doors = ''

            if (temporary_instance_e.e_lab_entrance is None):
                temporary_instance_e.e_lab_entrance = ''

            if (temporary_instance_e.e_ed_entrance is None):
                temporary_instance_e.e_ed_entrance = ''

            if (temporary_instance_e.e_monitor is None):
                temporary_instance_e.e_monitor = ''

            if (temporary_instance_e.e_directors is None):
                temporary_instance_e.e_directors = ''

            if (temporary_instance_e.e_runners is None):
                temporary_instance_e.e_runners = ''

            if (temporary_instance_e.e_num_staff is None):
                temporary_instance_e.e_num_staff = ''

            temporary_instance_e.save()

            context['east_lobby'] = East_Lobby.objects.all().order_by('-id')[:1]

        except:
            pass

        try:
            if context['east_lobby'][0].e_explain is True:
                context['e_explainval'] = 'Yes'
            else:
                context['e_explainval'] = 'No'
        except:
            pass

        if ((Town_Centre.objects.last().t_date == timezone.now().date()) and
           ((abs(int(Town_Centre.objects.last().t_time[0:2]) - int(str(datetime.datetime.now().time())[0:2])) == 0)) or
           ( (abs(int(Town_Centre.objects.last().t_time[0:2]) - int(str(datetime.datetime.now().time())[0:2])) == 1) and (int(Town_Centre.objects.last().t_time[3:5]) > int(str(datetime.datetime.now().time())[3:5])) )):

            temporary_instance_t = Town_Centre.objects.last() # last() doesn't return a Queryset!!!

        else:
            temporary_instance_t = None

        try:

            if (temporary_instance_t.t_time is None):
                temporary_instance_t.t_time = ''

            if (temporary_instance_t.t_coordinator is None):
                temporary_instance_t.t_coordinator = ''

            if (temporary_instance_t.t_horticultural is None):
                temporary_instance_t.t_horticultural = ''

            if (temporary_instance_t.t_town_centre_main_street is None):
                temporary_instance_t.t_town_centre_main_street = ''

            if (temporary_instance_t.t_monitor is None):
                temporary_instance_t.t_monitor = ''

            if (temporary_instance_t.t_directors is None):
                temporary_instance_t.t_directors = ''

            if (temporary_instance_t.t_runners is None):
                temporary_instance_t.t_runners = ''

            if (temporary_instance_t.t_num_staff is None):
                temporary_instance_t.t_num_staff = ''

            temporary_instance_t.save()

            context['town_centre'] = Town_Centre.objects.all().order_by('-id')[:1]

        except:
            pass

        try:
            if context['town_centre'][0].t_explain is True:
                context['t_explainval'] = 'Yes'
            else:
                context['t_explainval'] = 'No'
        except:
            pass

        return context


def about(request):

    context=None

    return render(request, 'index.html', context=context)


@login_required
def code_red_status(request):

    if request.method == 'GET':
        try:
            code_red_status = CodeStatuses.objects.last().code_red_status
            status_setter = CodeStatuses.objects.last().status_setter

            try:
                from_location = CodeStatuses.objects.last().from_location
            except:
                from_location = ''

            try:
                to_location = CodeStatuses.objects.last().to_location
            except:
                to_location = ''

        except: # If any of the first two are None...

            code_red_status_instance = CodeStatuses()

            code_red_status_instance.code_red_status = 'Normal'
            code_red_status_instance.status_setter = 'Unspecified'
            code_red_status_instance.from_location = ''
            code_red_status_instance.to_location = ''

            code_red_status_instance.save()

            code_red_status = 'Normal'
            status_setter = 'Unspecified'
            from_location = ''
            to_location = ''

        return JsonResponse({'code_red_status': code_red_status, 'status_setter': status_setter, 'from_location': from_location, 'to_location': to_location})

    elif request.method == 'POST': # Shouldn't need to TRY/EXCEPT or to save. Should be done on GET
        try:

            code_red_status_instance = CodeStatuses.objects.all()[0]
            # print(code_red_status_instance.from_location)

            code_red_status_instance.code_red_status = request.POST['code_red_status']
            code_red_status_instance.status_setter = request.POST['status_setter']

            try:
                code_red_status_instance.from_location = request.POST['from_location']
            except:
                code_red_status_instance.from_location = ''

            try:
                code_red_status_instance.to_location = request.POST['to_location']
            except:
                code_red_status_instance.to_location = ''

        except:
            code_red_status_instance = CodeStatuses()

        code_red_status_instance.save()

        return HttpResponse()
