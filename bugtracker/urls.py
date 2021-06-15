"""bugtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication.views import login_view, logout_view
from home.views import index_view
from ticket.views import create_ticket, ticket_detail, assigned, completed, invalid, edit_ticket
from home.views import user_detail

urlpatterns = [
    path('invalid/<int:ticket_id>/', invalid),
    path('complete/<int:ticket_id>/', completed),
    path('assign/<int:ticket_id>/', assigned),
    path('user/<int:user_id>/', user_detail),
    path('ticket/<int:ticket_id>/', ticket_detail, name='ticket'),
    path('ticket/<int:ticket_id>/edit/', edit_ticket),
    path('createticket/', create_ticket, name='create'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('', index_view, name='home'),
    path('admin/', admin.site.urls),
]
