from django.shortcuts import render, HttpResponseRedirect, reverse
from ticket.forms import CreateTicket
from ticket.models import Ticket

# Create your views here.


def create_ticket(request):
    if request.method == "POST":
        form = CreateTicket(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_ticket = Ticket.objects.create(
                title=data['title'], description=data['description'], filed=request.user)

            return HttpResponseRedirect(reverse('home'))

    form = CreateTicket()
    return render(request, 'ticketsub.html', {'form': form})


def edit_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)

    if request.method == "POST":
        form = CreateTicket(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.title = data['title']
            ticket.description = data['description']
            ticket.save()
            return HttpResponseRedirect(reverse('home'))

    form = CreateTicket(
        initial={'title': ticket.title, 'description': ticket.description})
    return render(request, 'ticketedit.html', {'form': form})


def ticket_detail(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'ticketdetail.html', {'ticket': ticket})


def assigned(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.assigned = request.user
    ticket.status = 'progress'
    ticket.completed = None
    ticket.save()

    return HttpResponseRedirect(reverse('home'))


def completed(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.completed = request.user
    ticket.status = 'done'
    ticket.assigned = None
    ticket.save()
    return HttpResponseRedirect(reverse('home'))


def invalid(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.status = 'invalid'
    ticket.assigned = None
    ticket.completed = None
    ticket.save()
    return HttpResponseRedirect(reverse('home'))
