from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index,name="ekstrakstok"),
    url(r'^save',views.save,name="saveekstrak"),

 ]