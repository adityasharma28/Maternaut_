from django.conf.urls import url
from . import views
   
app_name = "childcare"

urlpatterns = [
    url(r'^$', views.childcare, name="home"),
    # url(r'^search/$', views.child_search, name="search")
]
