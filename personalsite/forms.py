from django import forms
from ckeditor.widgets import CKEditorWidget
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=CKEditorWidget())
    captcha = CaptchaField()
