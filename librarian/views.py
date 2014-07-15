# from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.contrib.auth import logout

from . import models


class BookListView(ListView):
    model = models.Book
    context_object_name = "books"
    template_name = "home.html"


def logout_view(request):
    logout(request)
    return redirect(reverse('home'))
