from django.conf.urls import url
from . import views
from views import (add,save,update,prints,index,edit,report,modalstok,getprice)

urlpatterns = [
    url(r'^$', index, name="dataPenjualan"),
    url(r'^add', add, name="jual"),
    url(r'^getprice/(\d+)/(\d+)$',getprice,name="getprice"),
    url(r'^save', save, name="saveJual"),
    url(r'^edit/(?P<data>.+)$', views.edit, name="editJual"),
    url(r'^update',update,name="updateJual"),
    url(r'^print/(?P<id>\d+)$', prints, name="print"),
    url(r'^report', report, name="reportjual"),
    url(r'^modalstok/(?P<id>\d+)$', modalstok, name="modalstok" ),
    # url

]