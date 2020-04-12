from django.conf.urls import url
from . import views

app_name = "home"
   
urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^save_location/$', views.save_location, name="save_location")
]
