from django import forms
from .models import FormSubmission

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class FormSubmissionForm(forms.ModelForm):
    class Meta:
        model = FormSubmission
        fields = '__all__'
