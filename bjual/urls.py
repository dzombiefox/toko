from django.conf.urls import url
from views import (save,GetJualJson,delete,tes)


urlpatterns = [

    url(r'^save',save,name="savebjual"),
    url(r'^getBarangJual/(?P<id>\d+)$',GetJualJson.as_view(),name="getBarangJual"),
    url(r'^delete/(?P<id>\d+)$', delete, name="deleteBarangJual"),
    url(r'^tes',tes,name="tes")

]