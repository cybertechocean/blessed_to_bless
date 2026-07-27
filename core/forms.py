from django import forms

from .models import ContactMessage, VolunteerApplication


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ("name", "email", "subject", "message")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@example.com"}),
            "subject": forms.TextInput(attrs={"placeholder": "How can we help?"}),
            "message": forms.Textarea(attrs={"placeholder": "Tell us a little more...", "rows": 5}),
        }


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = VolunteerApplication
        fields = ("name", "email", "phone", "area_of_interest", "message")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@example.com"}),
            "phone": forms.TextInput(attrs={"placeholder": "+243 ..."}),
            "area_of_interest": forms.TextInput(attrs={"placeholder": "e.g. Education, communications"}),
            "message": forms.Textarea(attrs={"placeholder": "What would you love to contribute?", "rows": 5}),
        }