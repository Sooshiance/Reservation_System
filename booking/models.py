from django.db import models
from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from datetime import timedelta
from django.contrib.auth.models import User

from booking.utils import passedDays


class Ticket(models.Model):
    title          = models.CharField(max_length = 100)
    duration       = models.DurationField()
    departure_time = models.TimeField()
    arrival_time   = models.TimeField()
    
    def __str__(self):
        return self.title


class DisableDate(models.Model):
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class ReserveTicket(models.Model):
    user           = models.ForeignKey(User, on_delete=models.CASCADE)
    title          = models.ManyToManyField(Ticket, blank=True)
    date           = models.DateField(validators=[passedDays])
    hour           = models.DurationField(blank=True, null=True)
    description    = models.TextField(null=True, blank=True)
    admin_approval = models.BooleanField(default=False)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.user.username} : {self.title}"
    
    def save(self, *args, **kwargs):
        if DisableDate.objects.filter(date=self.date).exists():
            raise ValueError("This date can't be choose!")
        return super().save(*args, **kwargs)


@receiver(m2m_changed, sender=ReserveTicket.title.through)
def update_hour(sender, instance, action, **kwargs):
    if action == "post_add" or action == "post_remove":
        total_duration = timedelta()
        for ticket in instance.title.all():
            total_duration += ticket.duration
            instance.hour = total_duration
            instance.save()
