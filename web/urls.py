from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin

from librarian import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r"^$",
        view=views.BookListView.as_view(),
        name="home"),
    url(r'^book/add/$',
        view=views.BookCreateView.as_view(),
        name='create_book'),
    url(r'^book/attach/(?P<pk>\d+)$',
        view=views.BookDetailView.as_view(),
        name='book_detail'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r"^attachments/", include("files.urls")),
    url(r'^admin/', include(admin.site.urls)),
)
