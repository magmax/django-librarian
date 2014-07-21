# -*- coding: utf-8 -*-

# from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth import logout

from braces.views import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    MultiplePermissionsRequiredMixin,
)

from . import models, forms


class BookListView(LoginRequiredMixin, ListView):
    model = models.Book
    context_object_name = "books"
    template_name = 'book_list.html'


class BookCreateView(LoginRequiredMixin, CreateView):
    model = models.Book
    context_object_name = "books"
    template_name = 'book_add.html'
    form_class = forms.BookForm

    def get_success_url(self):
        return reverse('home')

class BookDetailView(DetailView):
    model = models.Book
    context_object_name = "book"
    template_name = "book_detail.html"

    def get_success_url(self):
        return reverse('home')


def logout_view(request):
    logout(request)
    return redirect(reverse('home'))
