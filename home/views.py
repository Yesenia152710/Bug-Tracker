
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ticket.models import Ticket
from authentication.models import Uzer

# Create your views here.


@login_required
def index_view(request):
    new = Ticket.objects.filter(status='new').order_by('time_date')
    progress = Ticket.objects.filter(status='progress').order_by('time_date')
    done = Ticket.objects.filter(status='done').order_by('time_date')
    invalid = Ticket.objects.filter(status='invalid').order_by('time_date')
    return render(request, 'index.html', {'new': new, 'pro': progress, 'done': done, 'inv': invalid})


def user_detail(request, user_id):
    user = Uzer.objects.get(id=user_id)
    assign_ticket = Ticket.objects.filter(assigned=user)
    filed_ticket = Ticket.objects.filter(filed=user)
    complete_ticket = Ticket.objects.filter(completed=user)
    return render(request, 'userdetail.html', {'user': user, 'filed': filed_ticket, 'assign': assign_ticket,
                                               'complete': complete_ticket})
