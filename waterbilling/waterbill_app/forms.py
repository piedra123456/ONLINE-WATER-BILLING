from django import forms
from .models import Consumerlist

class ConsumerlistForm(forms.ModelForm):
    class Meta:
        model = Consumerlist
        fields = "__all__"
