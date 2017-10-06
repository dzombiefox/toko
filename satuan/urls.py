from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index,name="satuan"),
    url(r'^add',views.add,name="addSatuan"),
    url(r'^save',views.save,name="saveSatuan"),
    url(r'^edit/(?P<data>.+)$',views.edit,name="editSatuan"),
    url(r'^update/(?P<id>\d+)$',views.update,name="updateSatuan"),
    url(r'^delete/(?P<data>.+)$',views.delete,name="deleteSatuan"),

]