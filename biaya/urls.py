from django.conf.urls import url
from views import (GetBiayaJson,save,delete)


urlpatterns = [
    # url(r'^$',views.index,name="harga"),
    # url(r'^add',views.add,name="addHarga"),
    url(r'^save',save,name="savebiaya"),
    url(r'^getBiaya/(?P<id>\d+)$',GetBiayaJson.as_view(),name="getBiaya"),
    # url(r'^edit/(?P<id>\d+)$',views.edit,name="editHarga"),
    # url(r'^update/(?P<id>\d+)$',views.update,name="updateJumlah"),
    url(r'^delete/(?P<id>\d+)$',delete,name="deleteBiaya"),

]