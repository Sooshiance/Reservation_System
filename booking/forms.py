from django import forms

from .models import ReserveTicket


class ReserveTicketForm(forms.ModelForm):
    
    class Meta:
        model = ReserveTicket
        fields = ['title', 'date']
