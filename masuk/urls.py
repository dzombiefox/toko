from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index,name="masuk"),
    url(r'^add',views.add,name="addMasuk"),
    url(r'^save',views.save,name="saveMasuk"),
    url(r'^edit/(?P<data>.+)$',views.edit,name="editMasuk"),
# url(r'^view/(?P<data>.+)$',views.index,name="butang"),
    # url(r'^edit/(?P<id>\d+)$', views.edit, name="editBarang"),
    url(r'^update/(?P<id>\d+)$',views.update,name="updateMasuk"),
    # url(r'^delete/(?P<id>\d+)$',views.delete,name="deleteSatuan"),

]