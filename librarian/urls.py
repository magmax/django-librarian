from django.conf.urls import include, patterns, url


urlpatterns = patterns(
    "librarian.views",
    url(r'^', include('web.urls')),
)
