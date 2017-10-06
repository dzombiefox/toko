from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^(?P<id>\d+)$',views.index,name="bhutang"),
    # url(r'^add',views.add,name="addMasuk"),
    url(r'^save',views.save,name="saveHutang"),

    # url(r'^edit/(?P<id>\d+)$',views.edit,name="editSatuan"),
    # url(r'^update/(?P<id>\d+)$',views.update,name="updateSatuan"),
    # url(r'^delete/(?P<id>\d+)$',views.delete,name="deleteSatuan"),

]