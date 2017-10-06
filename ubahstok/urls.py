from django.conf.urls import url
from views import (save,index)


urlpatterns = [
    url(r'^$', index, name="ubahstok"),
    url(r'^save',save,name="saveubahstok"),
    # url(r'^getBarangJual/(?P<id>\d+)$',GetJualJson.as_view(),name="getBarangJual"),
    # url(r'^delete/(?P<id>\d+)$', delete, name="deleteBarangJual"),
    # url(r'^tes',tes,name="tes")

]