from django import forms
from .models import Subscriber
from .models import Newsletter

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['subject', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }