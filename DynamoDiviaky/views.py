from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import HraciePlochy, Rezervacie, Hraci
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth import *
from django import forms
from django.http import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
import datetime
import pandas as pd

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/')
    return render(request,'login.html', context)

class Social(TemplateView):
    template_name = "DynamoDiviaky/social.html"

@login_required
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            # Akékoľvek ďalšie operácie s rezerváciou
            reservation.save()
        #    return redirect('reservation_create')
            return render(request, 'DynamoDiviaky/success.html')
    else:
        form = ReservationForm()
    return render(request, 'DynamoDiviaky/create.html', {'form': form})

@login_required
def reservation_success(request):
    return render(request, 'DynamoDiviaky/success.html')

@login_required
def home(request):
    return render(request, 'DynamoDiviaky/home.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def reztmp_list(request):
    # Získajte všetky položky
    rezervacia = Rezervacie.objects.all()
    # Aplikujte filter, ak je poslaný v požiadavke
    filter_param = request.GET.get('filter')
    if filter_param:
        rezervacia = rezervacia.filter(date=filter_param)
    return render(request, 'DynamoDiviaky/rez_list.html', {'rezervacia': rezervacia})
@login_required
def rez_detail(request, rez_id):
    rez = get_object_or_404(HraciePlochy, id=rez_id)

    return render(request, 'DynamoDiviaky/rez_detail.html', {'rez': rez})

@login_required
def rez_list(request):
#    # Získajte všetky položky
    sql_query = "SELECT R.id,R.date,R.start_time,R.end_time,I.nazov ihrisko ,T.skratka,Z.nazov typ  FROM \"DynamoDiviaky_rezervacie\" R INNER JOIN \"DynamoDiviaky_hracieplochy\" I ON I.id = R.hracieplochy_id INNER JOIN \"DynamoDiviaky_timy\" T  ON T.id = R.tim_id INNER JOIN \"DynamoDiviaky_typzapasu\" Z  ON Z.id = R.typzapasu_id WHERE date=%s "
    #AND field2 = %s"
    rezervacia = Rezervacie.objects.raw(sql_query, ['now()'])
#    rezervacia = Rezervacie.objects.all()
#    # Aplikujte filter, ak je poslaný v požiadavke
    filter_param = request.GET.get('filter')
    if filter_param:
         sql_query = "SELECT R.id,R.date,R.start_time,R.end_time,I.nazov ihrisko ,T.skratka,Z.nazov typ  FROM \"DynamoDiviaky_rezervacie\" R INNER JOIN \"DynamoDiviaky_hracieplochy\" I ON I.id = R.hracieplochy_id INNER JOIN \"DynamoDiviaky_timy\" T  ON T.id = R.tim_id INNER JOIN \"DynamoDiviaky_typzapasu\" Z  ON Z.id = R.typzapasu_id WHERE date=%s "
         rezervacia = Rezervacie.objects.raw(sql_query, [filter_param])
    else:
         sql_query = "SELECT R.id,R.date,R.start_time,R.end_time,I.nazov ihrisko ,T.skratka,Z.nazov typ  FROM \"DynamoDiviaky_rezervacie\" R INNER JOIN \"DynamoDiviaky_hracieplochy\" I ON I.id = R.hracieplochy_id INNER JOIN \"DynamoDiviaky_timy\" T  ON T.id = R.tim_id INNER JOIN \"DynamoDiviaky_typzapasu\" Z  ON Z.id = R.typzapasu_id"
         rezervacia = Rezervacie.objects.raw(sql_query)
    return render(request, 'DynamoDiviaky/rez_list.html', {'rezervacia': rezervacia, 'sql_query':sql_query})


def show_data(request):
    form = HraciFilterForm(request.GET or None)
    
    #hracis = []
    data = Hraci.objects.all()

    if request.method == 'GET' and form.is_valid():
        ftim  = form.cleaned_data.get('filter_tim')
        faktivita = form.cleaned_data.get('filter_aktivita')

        if ftim:
            data = data.filter(tim=ftim)
        if faktivita:
            data = data.filter(aktivita=faktivita)

    sort_by=request.GET.get('sort','datum_narodenia')
    data = data.order_by(sort_by)
    return render(request, 'DynamoDiviaky/show_data.html', { 'form' : form, 'data': data, })

def edit_data(request, pk):
    instance = get_object_or_404(Hraci, pk=pk)
    form = HraciForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        form = HraciForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('DynamoDiviaky:show_data')
    else:
        form = HraciForm(instance=instance)
    return render(request, 'DynamoDiviaky/edit_data.html', {'form': form})

def insert_data(request):
    form = HraciForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('show_data')
    return render(request, 'DynamoDiviaky/insert_data.html', {'form': form})

def update_item(request, item_id):
    item = Hraci.objects.get(id=item_id)
    new_aktivita = request.POST.get('new_aktivita')

    if new_name:
        item.aktivita = new_aktivita
        item.save()

        # Return a success response
        return JsonResponse({'status': 'success'})

    # Return an error response if the new name is empty
    return JsonResponse({'status': 'error', 'message': 'Invalid data'})


def generate_matches(teams, start_time, match_duration, break_duration):
    num_teams = len(teams)
    num_rounds = num_teams - 1

    match_time = start_time
    all_matches = []
    for round in range(num_rounds):
        matches = []
        for i in range(num_teams // 2):
            team1 = teams[i]
            team2 = teams[num_teams - 1 - i]

            match_end_time = match_time + timedelta(minutes=match_duration)
            matches.append((team1, team2, match_time, match_end_time))

            match_time = match_end_time + timedelta(minutes=break_duration)

        teams.insert(1, teams.pop())

        all_matches.append(matches)

    return all_matches

## Zoznam mužstiev
#teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']

## Časové údaje
#start_time = datetime.strptime('9:00', '%H:%M')
#match_duration = 20
#break_duration = 5

## Vygenerovanie zápasov
#matches = generate_matches(teams, start_time, match_duration, break_duration)

## Výpis všetkých zápasov
#for round, matches_round in enumerate(matches, start=1):
#    print(f"Round {round}:")
#    for match in matches_round:
#        match_start_time = match[2].strftime('%H:%M')
#        match_end_time = match[3].strftime('%H:%M')
#        print(f"{match[0]} vs {match[1]} ({match_start_time} - {match_end_time})")

def export_to_excel(data_list, file_path):
    # Convert the list to a DataFrame
    df = pd.DataFrame(data_list)
    
    # Write the DataFrame to an Excel file
    df.to_excel(file_path)
