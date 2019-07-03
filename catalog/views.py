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
        # print(request.POST['c'])
        if Cafeteria.objects.last() is None:
            cafeteria_instance = Cafeteria()
            print(type(cafeteria_instance))
            print(cafeteria_instance)
        else:
            if ((Cafeteria.objects.last().c_date == timezone.now().date()) and (abs(int(Cafeteria.objects.last().c_time[0:2]) - int(str(datetime.datetime.now().time())[0:2])) < 2)):
                cafeteria_instance = Cafeteria.objects.all().order_by('-id')[:1][0]
            else:
                cafeteria_instance = Cafeteria()

        # Create a form instance and populate it with data from the request (binding):
        form_c = CafeteriaForm(request.POST)
        print(form_c.errors)
        # print(form_c.cleaned_data['c_time'])
        # Check if the form is valid:
        if form_c.is_valid():
            print('valid')
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            cafeteria_instance.c_date = form_c.cleaned_data['c_date']

            # if form_c.cleaned_data['c_time'].strip() != '':
            # print(form_c.cleaned_data['c_time'])
            cafeteria_instance.c_time = form_c.cleaned_data['c_time']#.strip()
            # if form_c.cleaned_data['c_coordinator'].strip() != '':
            cafeteria_instance.c_coordinator = form_c.cleaned_data['c_coordinator'].strip()

            # if form_c.cleaned_data['c_main_doors'].strip() != '':
            cafeteria_instance.c_main_doors = form_c.cleaned_data['c_main_doors'].strip()
            # if form_c.cleaned_data['c_south_patio_doors'].strip() != '':
            cafeteria_instance.c_south_patio_doors = form_c.cleaned_data['c_south_patio_doors'].strip()
            # if form_c.cleaned_data['c_north_patio_doors_1'].strip() != '':
            cafeteria_instance.c_north_patio_doors_1 = form_c.cleaned_data['c_north_patio_doors_1'].strip()
            # if form_c.cleaned_data['c_north_patio_doors_2'].strip() != '':
            cafeteria_instance.c_north_patio_doors_2 = form_c.cleaned_data['c_north_patio_doors_2'].strip()

            # if form_c.cleaned_data['c_monitor'].strip() != '':
            cafeteria_instance.c_monitor = form_c.cleaned_data['c_monitor'].strip()
            # if form_c.cleaned_data['c_directors'].strip() != '':
            cafeteria_instance.c_directors = form_c.cleaned_data['c_directors'].strip()
            # if form_c.cleaned_data['c_runners'].strip() != '':
            cafeteria_instance.c_runners = form_c.cleaned_data['c_runners'].strip()
            # if form_c.cleaned_data['c_explain'] != '':

            cafeteria_instance.c_num_staff = form_c.cleaned_data['c_num_staff'].strip()

            cafeteria_instance.c_explain = form_c.cleaned_data['c_explain']

            cafeteria_instance.save()

        # redirect to a new URL:
        return HttpResponseRedirect(reverse('LIVE') )

    # If this is a GET (or any other method) create the default form.
    else:

        try:
            if ((Cafeteria.objects.last().c_date == timezone.now().date()) and (abs(int(Cafeteria.objects.last().c_time[0:2]) - int(str(datetime.datetime.now().time())[0:2])) < 2)):

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

    try:
        east_lobby_instance = East_Lobby.objects.get(pk=timezone.now())
    except:
        east_lobby_instance = East_Lobby()

    if request.method == 'POST' and 'e' in request.POST:

        # Create a form instance and populate it with data from the request (binding):
        form_e = East_LobbyForm(request.POST)

        # Check if the form is valid:
        if form_e.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            east_lobby_instance.e_date = form_e.cleaned_data['e_date']

            # if form_e.cleaned_data['e_time'].strip() != '':
            east_lobby_instance.e_time = form_e.cleaned_data['e_time'].strip()
            # if form_e.cleaned_data['e_coordinator'].strip() != '':
            east_lobby_instance.e_coordinator = form_e.cleaned_data['e_coordinator'].strip()

            # if form_e.cleaned_data['e_main_doors'].strip() != '':
            east_lobby_instance.e_main_doors = form_e.cleaned_data['e_main_doors'].strip()
            # if form_e.cleaned_data['e_lab_entrance'].strip() != '':
            east_lobby_instance.e_lab_entrance = form_e.cleaned_data['e_lab_entrance'].strip()
            # if form_e.cleaned_data['e_ed_entrance'].strip() != '':
            east_lobby_instance.e_ed_entrance = form_e.cleaned_data['e_ed_entrance'].strip()

            # if form_e.cleaned_data['e_monitor'].strip() != '':
            east_lobby_instance.e_monitor = form_e.cleaned_data['e_monitor'].strip()
            # if form_e.cleaned_data['e_directors'].strip() != '':
            east_lobby_instance.e_directors = form_e.cleaned_data['e_directors'].strip()
            # if form_e.cleaned_data['e_runners'].strip() != '':
            east_lobby_instance.e_runners = form_e.cleaned_data['e_runners'].strip()

            east_lobby_instance.e_num_staff = form_e.cleaned_data['e_num_staff'].strip()

            # if form_e.cleaned_data['e_explain'] != '':
            east_lobby_instance.e_explain = form_e.cleaned_data['e_explain']


            east_lobby_instance.save()

        # redirect to a new URL:
        return HttpResponseRedirect(reverse('LIVE') )

    # If this is a GET (or any other method) create the default form.
    else:

        try:
            e_time = East_Lobby.objects.get(pk=timezone.now()).e_time
        except:
            e_time = ''

        try:
            e_coordinator = East_Lobby.objects.get(pk=timezone.now()).e_coordinator
        except:
            e_coordinator = ''

        try:
            e_main_doors = East_Lobby.objects.get(pk=timezone.now()).e_main_doors
        except:
            e_main_doors = ''

        try:
            e_lab_entrance = East_Lobby.objects.get(pk=timezone.now()).e_lab_entrance
        except:
            e_lab_entrance = ''

        try:
            e_ed_entrance = East_Lobby.objects.get(pk=timezone.now()).e_ed_entrance
        except:
            e_ed_entrance = ''

        try:
            e_monitor = East_Lobby.objects.get(pk=timezone.now()).e_monitor
        except:
            e_monitor = ''

        try:
            e_directors = East_Lobby.objects.get(pk=timezone.now()).e_directors
        except:
            e_directors = ''

        try:
            e_runners = East_Lobby.objects.get(pk=timezone.now()).e_runners
        except:
            e_runners = ''

        try:
            e_num_staff = East_Lobby.objects.get(pk=timezone.now()).e_num_staff
        except:
            e_num_staff = ''

        try:
            e_explain = East_Lobby.objects.get(pk=timezone.now()).e_explain
        except:
            e_explain = ''

        form_e = East_LobbyForm(initial={'e_date': timezone.now(),
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

    # Render the HTML template with the data in the context variable
    return render(request, 'east_lobby_form.html', context=context)

# ==================================================================================================

@login_required
def town_centre_form(request):
    '''View function for home page of site.'''

    num_events = Town_Centre.objects.all().count() # All is implied by default

    try:
        town_centre_instance = Town_Centre.objects.get(pk=timezone.now())
    except:
        town_centre_instance = Town_Centre()

    if request.method == 'POST' and 't' in request.POST:

        # Create a form instance and populate it with data from the request (binding):
        form_t = Town_CentreForm(request.POST)

        # Check if the form is valid:
        if form_t.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            town_centre_instance.t_date = form_t.cleaned_data['t_date']

            # if form_t.cleaned_data['t_time'].strip() != '':
            town_centre_instance.t_time = form_t.cleaned_data['t_time'].strip()
            # if form_t.cleaned_data['t_coordinator'].strip() != '':
            town_centre_instance.t_coordinator = form_t.cleaned_data['t_coordinator'].strip()

            # if form_t.cleaned_data['t_horticultural'].strip() != '':
            town_centre_instance.t_horticultural = form_t.cleaned_data['t_horticultural'].strip()
            # if form_t.cleaned_data['t_town_centre_main_street'].strip() != '':
            town_centre_instance.t_town_centre_main_street = form_t.cleaned_data['t_town_centre_main_street'].strip()

            # if form_t.cleaned_data['t_monitor'].strip() != '':
            town_centre_instance.t_monitor = form_t.cleaned_data['t_monitor'].strip()
            # if form_t.cleaned_data['t_directors'].strip() != '':
            town_centre_instance.t_directors = form_t.cleaned_data['t_directors'].strip()
            # if form_t.cleaned_data['t_runners'].strip() != '':
            town_centre_instance.t_runners = form_t.cleaned_data['t_runners'].strip()

            town_centre_instance.t_num_staff = form_t.cleaned_data['t_num_staff'].strip()

            # if form_t.cleaned_data['t_explain'] != '':
            town_centre_instance.t_explain = form_t.cleaned_data['t_explain']


            town_centre_instance.save()

        # redirect to a new URL:
        return HttpResponseRedirect(reverse('LIVE') )

    # If this is a GET (or any other method) create the default form.
    else:

        try:
            t_time = Town_Centre.objects.get(pk=timezone.now()).t_time
        except:
            t_time = ''

        try:
            t_coordinator = Town_Centre.objects.get(pk=timezone.now()).t_coordinator
        except:
            t_coordinator = ''

        try:
            t_horticultural = Town_Centre.objects.get(pk=timezone.now()).t_horticultural
        except:
            t_horticultural = ''

        try:
            t_town_centre_main_street = Town_Centre.objects.get(pk=timezone.now()).t_town_centre_main_street
        except:
            t_town_centre_main_street = ''

        try:
            t_monitor = Town_Centre.objects.get(pk=timezone.now()).t_monitor
        except:
            t_monitor = ''

        try:
            t_directors = Town_Centre.objects.get(pk=timezone.now()).t_directors
        except:
            t_directors = ''

        try:
            t_runners = Town_Centre.objects.get(pk=timezone.now()).t_runners
        except:
            t_runners = ''

        try:
            t_num_staff = Town_Centre.objects.get(pk=timezone.now()).t_num_staff
        except:
            t_num_staff = ''

        try:
            t_explain = Town_Centre.objects.get(pk=timezone.now()).t_explain
        except:
            t_explain = ''

        form_t = Town_CentreForm(initial={'t_date': timezone.now(),
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

    # Render the HTML template with the data in the context variable
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

        temporary_instance = Cafeteria.objects.last() # last() doesn't return a Queryset!!!

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











        context['east_lobby'] = East_Lobby.objects.filter(e_date=timezone.now())

        try:
            if context['east_lobby'][0].e_explain is True:
                context['e_explainval'] = 'Yes'
            else:
                context['e_explainval'] = 'No'
        except:
            pass












        context['town_centre'] = Town_Centre.objects.filter(t_date=timezone.now())

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



def code_red_status(request):

    if request.method == 'GET':
        try:
            code_red_status = CodeStatuses.objects.last().code_red_status
            status_setter = CodeStatuses.objects.last().status_setter
            from_location = CodeStatuses.objects.last().from_location
            to_location = CodeStatuses.objects.last().to_location
        except:
            code_red_status = ''
            status_setter = ''
            from_location = ''
            to_location = ''

        # code_red_status = code_red_status.code_red_status
        # print(code_red_status.code_red_status)
        # print(status_setter)
        # print(from_location)
        # status_setter = code_red_status.status_setter
        # from_location = code_red_status['from_location']
        # to_location = code_red_status.to_location
        # print(CodeStatuses.objects.all()[0])
        # response_data = {}
        # response_data['code_status'] = CodeStatuses.objects.all()[0]
        # response_data['message'] = 'My message'
        # response_instance = HttpResponse()
        # response_instance['code_red_status'] = context['code_red_status']
        # context = {'key', 'value'}
        # print (context['code_red_status'])
        # return HttpResponse(context)
        return JsonResponse({'code_red_status': code_red_status, 'status_setter': status_setter, 'from_location': from_location, 'to_location': to_location})

    elif request.method == 'POST':
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

            # print('OKOKOKOKOKOOKOKOKOK')
            # CodeStatuses.objects.last().code_red_status = request.POST['code_red_status']
            # CodeStatuses.objects.last().status_setter = request.POST['status_setter']
            # CodeStatuses.objects.last().from_location = request.POST['from_location']
            # CodeStatuses.objects.last().to_location = request.POST['to_location']
        except:
            code_red_status_instance = CodeStatuses()
        # print(code_red_status_instance)
        # Assign to the database the new value



        code_red_status_instance.save()

        return HttpResponse()
