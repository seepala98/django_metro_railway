from django.shortcuts import get_list_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import UserForm
from booking.models import Train, Ticket
from booking.forms import TicketForm
from booking.utils import class_name, update_count
from .models import *

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/index/')

    context = {
        "form": form,
    }
    return render(request,'register.html', context)

def logout_user(request):

    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request,'login.html',context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'index.html',{})
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')



def index(request):
    if request.user.is_authenticated():
        return render(request,'index.html')
    else:
        form = UserForm(request.POST or None)
        context = {
        "form": form,
        }
        return render(request,'login.html',context)

def search_results(request):
    ''' Display search results filter by queries '''
    trains = get_list_or_404(Train.objects.filter(
        date=request.GET.get('date'),
        route__source__name=request.GET.get('source'),
        route__destination__name=request.GET.get('destination'),
    ))
    context = {'trains': trains}
    return render(request, 'search.html', context)


def book_ticket(request):
    ''' Book Tikcet'''
    if request.method == 'GET':
        form = TicketForm()
        train = Train.objects.get(pk=request.GET.get('train'))
        seat_class = request.GET.get('class')
        train_context = {
            'train': train,
            'class_model_name': seat_class,
            'class': class_name(seat_class),
            'seat': getattr(train, seat_class)
        }
    elif request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            train = Train.objects.get(pk=request.POST.get('train'))
            form.instance.train = train
            instance = form.save()
            # update count
            update_count(train, request.POST.get('class'))
            return HttpResponseRedirect(reverse('booking:get_ticket', args=(instance.id,)))
    else:
        return HttpResponseRedirect('/')

    return render(request, 'booking.html', {'form': form, 'train_context': train_context})


def ticketdetails(request,ticket_id):
    a=Ticket.objects.get(id=ticket_id)
    traindet=a.train
    b=Train.objects.get(name=traindet)
    routename=b.route
    c=Route.objects.get(name=routename)
    source=c.source
    dest=c.destination
    trainsdet=Ticket.objects.get(id=ticket_id)
    f = Train.objects.get(number = b.number)
    fare = f.fare
    context={
    'source':source,
    'dest':dest,
    'trainsdet':trainsdet,
    'fare':fare,
    }
    return render(request,'completeticket.html',context) 


def aboutus(request):
    return render(request,'aboutus.html',{})

def stationinfo(request):
    return render(request,'stationinfo.html',{})


class GetTicket(DetailView):
    model = Ticket
    template_name = 'ticket.html'
    context_object_name = 'ticket'
