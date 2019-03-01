from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *

from instamojo_wrapper import Instamojo

API_KEY = 'f1761e15f5415be96a7248dea2bbdaf0'
AUTH_TOKEN = 'f509e1c1b11e28cad3260de8620b1456'


def clean_data(data_dict):
    for key in data_dict.keys():
        data_dict[key] = data_dict[key][0]

    return data_dict

# Create your views here.
#All get related links are displayed in acuthon itself using modals or some divs
#All other views are just for handling POST data
def acuthon(request, *args, **kwargs):
    print(kwargs)
    payment_status = "Pending"
    participants = None
    paid = False
    participant = None
    user = None
    team = None
    if request.user.is_authenticated:
        user = request.user
        try:
            participant = Participant.objects.get(user=request.user)
            team = participant.team
            if team is not None:
                participants = [p.user.email for p in team.participant_set.filter()[:4]]
            if participant.payment:
                payment_status = participant.payment.payment_status
            if payment_status == "Credit":
                paid = True
        except:
            pass
         
    return render(request, 'homepage.html', context={
        'participant': participant,
        'user': user,
        'team': team,
        'participants': participants,
        'payment_status': payment_status,
        'paid': paid,
        **kwargs
    })

def logout_view(request):
    logout(request)
    return redirect('/acuthon')

def register(request):
    """
    POST:
    Create a User
    After successful user creation create participant
    Get the extra details needed for participant model
    Commit the changes and data to DB
    Login the user
    """
    if request.method == 'POST':
        fname = request.POST.get('first_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile_number = request.POST.get('mobile_number')
        college = request.POST.get('college')
    
        user = User.objects.create_user(username=email,email=email,password=password,first_name=fname)
        participant = Participant(user=user,college=college,contact =mobile_number)
        participant.save()
        login(request,user)
        return redirect('/acuthon?redirect=true&registered=true')
        

def login_view(request):
    """
    POST:
    Check if the credentials are correct then login the user
    """
    if request.method == 'POST':
       # user = User.objects.create_user(**request.POST)
        
        user = authenticate(username = request.POST.get('email'),password = request.POST.get('password'))
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect("/acuthon?redirect=true&login=true")
            else:
                pass
        else:
            return redirect("/acuthon?redirect=true&loginfailed=true")
        return HttpResponse("Received")

@login_required(login_url='/acuthon/login')
def team(request):
    if request.method == 'POST':
        form_data = clean_data(dict(request.POST))
        theme = form_data['theme']
        team = Team.objects.get(name=form_data['name'])
        team.theme = form_data['theme']
        team.project_link = form_data['project_link']
        team.save()
        participants = [
            form_data['participant1'],
            form_data['participant2'],
            form_data['participant3'],
            form_data['participant4']
        ]
        for participant in participants:
            try:
                participant_obj = Participant.objects.get(user__email=participant)
                participant_obj.team = team
                participant_obj.save()
            except:
                return redirect('/acuthon?redirect=true&teamupdate=false')
        return redirect('/acuthon?redirect=true&teamupdate=true')


@login_required(login_url='/acuthon/login')
def team_leave(request):
    """
    Leave team
    """
    if request.method == 'POST':
        participant = Participant.objects.get(user=request.user)
        participant.team = None
        participant.save()
        return redirect('/acuthon?redirect=true&leave=true')

@login_required(login_url='/acuthon/login')
def team_create(request):
    """
    POST:
    Create team and add participants as CSV
    """
    if request.method == 'POST':
        try:
            new_team = Team.objects.create(
                name=request.POST.get('name'),
                team_lead = request.user.email
            )
            new_team.save()
            print(new_team.name, new_team.team_lead)
            participant = request.user.participant
            participant.team = new_team
            participant.save()
        except:
            return redirect('/acuthon?redirect=true&teamcreate=false')            
        return redirect('/acuthon?redirect=true&teamcreate=true')

@login_required(login_url='/acuthon/login')
def team_join(request):
    """
    POST:
    Create team and add participants
    """
    if request.method == 'POST':
        try:
            team = Team.objects.get(
                name=request.POST.get('name')
            )
            participant = request.user.participant
            print(team.participant_set.filter().__len__())
            if team.participant_set.filter().__len__() < 4 and participant.team is None:
                participant.team = team
                participant.save()
            else:
                raise ArithmeticError('Count exceeded')
        except:
            return redirect('/acuthon?redirect=true&join=false')
        
        return redirect('/acuthon?redirect=true&join=true')

@login_required(login_url='/acuthon/login')
def participant(request):
    """
    POST:
    Create team and add participants as CSV
    """
    if request.method == 'POST':
        form_data = clean_data(dict(request.POST))
        request.user.first_name = form_data['first_name']
        request.user.email = form_data['email']
        request.user.save()
        participant = request.user.participant
        participant.college = form_data['college']
        participant.branch = form_data['branch']
        participant.contact = form_data['contact']
        participant.save()
        return redirect('/acuthon?redirect=true&update=true')        


#Move the creation of Payment to record to payment_webhook
def payment_response(request):
    '''
    An acknowledgment page for the user about the payment status.
    (May use the index page and show the status)
    '''
    payment = Payment(user = request.user,payment_id =request.GET.get('payment_id'),
    payment_status = request.GET.get('payment_status'),payment_request_id=request.GET.get('payment_request_id'))
    payment.save()
    
    if request.GET.get('payment_status') == 'Credit':
        return HttpResponse("Payment is successful!")
    elif request.GET.get('payment_status') == 'Failed':
        return HttpResponse("Payment Failed!")
    else:
        return HttpResponse("Wrong output!")


def payment_request(request):
    '''
    Creates a payment request and redirects to instamojo payments page and on completion returns to payment_response page.
    '''
    api = Instamojo(api_key=API_KEY,
                auth_token=AUTH_TOKEN)
    
    participant = Participant.objects.get(user=request.user)
    response = api.payment_request_create(
        amount='150',
        purpose='Acument IT Hackathon',
        buyer_name = request.user.first_name,
        send_email=True,
        email=request.user.email,
        phone=participant.contact,
        redirect_url="http://localhost:8000/acuthon/payment_response",
        webhook = "http://vceresults.pythonanywhere.com/check"
    )

    print(response['payment_request']['id'])

    return redirect(response['payment_request']['longurl'])


#For webhook from instamojo
def payment_webhook(request):
    print(request.POST)
    '''
    An acknowledgment page for the user about the payment status.
    (May use the index page and show the status)
    '''
    payment = Payment(user = request.user,payment_id =request.GET.get('payment_id'),
    payment_status = request.GET.get('payment_status'),payment_request_id=request.GET.get('payment_request_id'))
    payment.save()
    
    if request.GET.get('payment_status') == 'Credit':
        return redirect('/acuthon/?redirect=true&payment=true')
    elif request.GET.get('payment_status') == 'Failed':
        return redirect('/acuthon/?redirect=true&payment=false')
    else:
        return HttpResponse("Wrong output!")


        