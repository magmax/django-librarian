# -*- coding: utf-8 -*-

import time
from django import forms
from django.conf import settings
from django.forms.util import ErrorDict
from django.utils.crypto import salted_hmac, constant_time_compare
from django.utils.translation import ugettext_lazy as _

from . import models


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ("isbn_13", "title", "description", "publisher",
                  "year", "language", "authors")
        _attrs = {'class':"form-control"}
        widgets = {
            'title': forms.TextInput(attrs=_attrs),
            'description': forms.Textarea(attrs=_attrs),
            'isbn_13': forms.TextInput(attrs=_attrs),
            'publisher': forms.TextInput(attrs=_attrs),
            'year': forms.TextInput(attrs=_attrs),
            'language': forms.TextInput(attrs=_attrs),
            'authors': forms.SelectMultiple(attrs=_attrs),
        }
