from django.utils import timezone
from django.core.exceptions import ValidationError


def passedDays(date):
    if date < timezone.now().date():
        raise ValidationError("")
    else:
        return date
