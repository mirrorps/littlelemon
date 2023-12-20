from django.forms import ModelForm
from .models import Booking
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
        widgets = {
            'reservation_date': DateInput(),
        }
