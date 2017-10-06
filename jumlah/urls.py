from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index,name="jumlah"),
    url(r'^add',views.add,name="addJumlah"),
    url(r'^save',views.save,name="saveJumlah"),
    url(r'^edit/(?P<data>.+)$',views.edit,name="editJumlah"),
    url(r'^update/(?P<id>\d+)$',views.update,name="updateJumlah"),
    url(r'^delete/(?P<data>.+)$',views.delete,name="deleteJumlah"),

]