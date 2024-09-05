from django.core import validators
from django import forms
from .models import Slots




class ModelFormSlot(forms.ModelForm):

    class Meta:
        model = Slots
        fields = ['block_name', 'number_of_slots', 'slot_type', ]

        widgets = {
            'block_name': forms.TextInput(attrs={
                'placeholder': 'Enter Block Name'
            }),
            'number_of_slots': forms.NumberInput(attrs={
                'placeholder': 'Enter Number of Slots'
            }),
            'slot_type': forms.Select(attrs={
                'placeholder': 'deadline'
            }),

        }





