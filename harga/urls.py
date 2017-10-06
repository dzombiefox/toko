from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index,name="harga"),
    url(r'^add',views.add,name="addHarga"),
    url(r'^save',views.save,name="saveHarga"),
    url(r'^edit/(?P<data>.+)$',views.edit,name="editHarga"),
    url(r'^update/(?P<id>\d+)$',views.update,name="updateJumlah"),
    url(r'^delete/(?P<data>.+)$',views.delete,name="deleteHarga"),

]