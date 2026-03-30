from django import forms
from .models import Friend
class AcharyaFriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['AUID', 'full_name', 'email']