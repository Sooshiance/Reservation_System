from django.db.models.signals import m2m_changed, pre_delete
from django.dispatch import receiver
from .models import ReserveTicket, Departure
from django.core.exceptions import ValidationError


@receiver(pre_delete, sender=ReserveTicket)
def restore_capacity_on_delete(sender, instance, **kwargs):
    departure = instance.date
    departure.capacity += 1
    departure.save()


@receiver(m2m_changed, sender=ReserveTicket.title.through)
def update_capacity_on_add(sender, instance, action, **kwargs):
    print(f"Signal triggered with action: {action}")
    if action == "post_add":
        departure = instance.date
        print(f"Departure before update: {departure.capacity}")
        if departure.capacity >= 0:
            departure.capacity -= 1
            departure.save()
            print(f"New departure capacity: {departure.capacity}")
        else:
            raise ValidationError(f"No capacity left for {departure.train.title} on {departure.date}")
