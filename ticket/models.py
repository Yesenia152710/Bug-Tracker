from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from authentication.models import Uzer


# Create your models here.


class Ticket(models.Model):
    TICKET_STATUS = [
        ('new', 'New'),
        ('progress', 'In Progress'),
        ('done', 'Done'),
        ('invalid', 'Invalid'),
    ]

    title = models.CharField(max_length=50)
    time_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    filed = models.ForeignKey(
        Uzer, null=True, on_delete=CASCADE, related_name="Filed")
    status = models.CharField(
        max_length=8, choices=TICKET_STATUS, default='new')
    assigned = models.ForeignKey(
        Uzer, null=True, on_delete=CASCADE, related_name="Assigned")
    completed = models.ForeignKey(
        Uzer, null=True, on_delete=CASCADE, related_name="Completed")
