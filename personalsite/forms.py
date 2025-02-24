from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
    hidden_input = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    verification = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    # def is_valid(self):
    #     if self.validator is not None or self.validator != "":
    #         return False
    #     return super().is_valid()
