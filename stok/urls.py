from django.conf.urls import url
from . import views
from views import (index,GetStokJson)
urlpatterns = [
	url(r'^$',views.index,name="stok"),
    url(r'^getStok/(?P<id>\d+)$',GetStokJson.as_view(),name="getStok"),
    # url(r'^add',views.add,name="addSuplier"),
    # url(r'^save',views.save,name="saveSupplier"),
    # url(r'^edit/(?P<data>.+)$',views.edit,name="editSuplier"),
    # url(r'^update/(?P<id>\d+)$',views.update,name="updateSuplier"),
    # url(r'^delete/(?P<data>.+)$',views.delete,name="deleteSuplier"),

]