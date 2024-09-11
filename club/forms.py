from typing import Any
from django import forms

from club.models import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['txt', 'vote']
    
    def clean(self):
        cleaned = super().clean()
        vote = cleaned["vote"]
        if 0 > vote > 5:
            raise ValueError()
        return cleaned
