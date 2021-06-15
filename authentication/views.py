from django.shortcuts import redirect, render, HttpResponseRedirect, reverse
from authentication.forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from authentication.models import Uzer
# Create your views here.


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            a_user = authenticate(request, username=data['username'],
                                  password=data['password'])
            if a_user:
                login(request, a_user)
                return HttpResponseRedirect(reverse('home'))

    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    log = logout(request)
    return redirect('home')
