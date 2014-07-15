from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin

from librarian import views
from .views import static_file

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r"^$",
        view=login_required(views.BookListView.as_view(),
                            login_url='/accounts/login/'),
        name="home"),
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
