from django import forms
from .models import *
from mongoengine.django.auth import *
from django.contrib.auth import authenticate, login, logout

class CommentForm(forms.Form):
    comment =  forms.CharField(widget = forms.Textarea, label="", required=True)

    def clean(self):
        comment = self.cleaned_data.get('comment')

        return super(CommentForm, self).clean()


        #check for bad words and spam detector
