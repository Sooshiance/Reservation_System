from django.db import models
from django.contrib.auth.models import User

from booking.models import Ticket


class FAQ(models.Model):
    title = models.CharField(max_length = 255)
    txt = models.TextField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Frequently Asked Question'
        verbose_name_plural = 'Frequently Asked Questions'


class Rating(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket     = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    txt        = models.TextField()
    vote       = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} about: {self.ticket}"
