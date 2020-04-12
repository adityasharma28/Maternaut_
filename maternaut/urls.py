from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^connect/', include('connect.urls')),
    url(r'^learn/', include('learn.urls')),
    url(r'^childcare/', include('childcare.urls')),
    url(r'about/$', views.about),
    url(r'^$', views.homepage, name="homepage")
]

urlpatterns += staticfiles_urlpatterns()
