from django import forms
from django.forms import ModelForm
from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book

        exclude = ('posted_by',)
