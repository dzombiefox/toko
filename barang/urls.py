from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index,name="barang"),
    url(r'^add',views.add,name="addBarang"),
    url(r'^save',views.save,name="saveBarang"),
    url(r'^edit/(?P<data>.+)$',views.edit,name="editBarang"),
    url(r'^update/(?P<id>\d+)$',views.update,name="updateBarang"),
    url(r'^delete/(?P<data>.+)$',views.delete,name="deleteBarang"),

]
