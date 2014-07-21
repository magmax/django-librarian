from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin

from librarian import views
from .views import static_file

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

    url(r'^accounts/login/$',
        'django.contrib.auth.views.login',
        {'template_name': 'login.html'},
        name='login'),
    url(r'^accounts/logout/$',
        view=views.logout_view,
        name='logout'),
    url(r'^assets/css/bootstrap',
        static_file,
        {'filename': 'static/vendor/bootstrap/dist/css/bootstrap.min.css'},
        name='css_bootstrap'),
    url(r"^attachments/", include("files.urls")),
    url(r'^admin/', include(admin.site.urls)),
)
