from django.conf.urls import url
from views import (GetBarangJson,save,delete)


urlpatterns = [
    # url(r'^$',views.index,name="harga"),
    # url(r'^add',views.add,name="addHarga"),
    url(r'^save',save,name="savebmasuk"),
    url(r'^getBarang/(?P<id>\d+)$',GetBarangJson.as_view(),name="getBarang"),
    # url(r'^edit/(?P<id>\d+)$',views.edit,name="editHarga"),
    # url(r'^update/(?P<id>\d+)$',views.update,name="updateJumlah"),
    url(r'^delete/(?P<id>\d+)$',delete,name="deleteBarang"),

]