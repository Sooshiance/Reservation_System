from django.db import models
from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from booking.utils import passedDays


class Ticket(models.Model):
    title     = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.title


class Departure(models.Model):
    date     = models.DateField(validators=[passedDays])
    capacity = models.PositiveIntegerField(default=0)
    train    = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.train} {self.date} {self.capacity}"


class ReserveTicket(models.Model):
    user           = models.ForeignKey(User, on_delete=models.CASCADE)
    title          = models.ManyToManyField(Ticket, blank=True)
    date           = models.ForeignKey(Departure, on_delete=models.CASCADE)
    admin_approval = models.BooleanField(default=False)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.user.username} : {self.title}"
