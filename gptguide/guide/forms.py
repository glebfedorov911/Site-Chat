from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.core.exceptions import ValidationError

from .models import *


class RegistrationForm(UserCreationForm):

    class Meta:
        model = UserCustomModel
        fields = ["username", "email", "password1", "password2"]

class RefForm(forms.Form):
    refcode = forms.CharField(max_length=8)

class MessageForm(forms.ModelForm):
    msg = forms.CharField(widget=forms.TextInput({"class": "send-msg", "placeholder": "Введите Ваше Сообщение"}), label=False)

    class Meta:
        model = Message
        fields = ("msg", )

class EditAdminForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput({"class": "avatar"}), required=False)
    instruction = forms.CharField(widget=forms.Textarea({"class": "instruction"}), required=False)
    doc = forms.FileField(widget=forms.FileInput({"class": "doc"}), required=False)
    url = forms.CharField(widget=forms.TextInput({"class": "url"}), required=False)
    token = forms.CharField(widget=forms.TextInput({"class": "token"}), required=False)

    class Meta:
        model = AdminPanelEdit
        fields = "__all__"

