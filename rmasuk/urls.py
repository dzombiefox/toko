from django.conf.urls import url
from . import views
from views import (GetReturJson,save,delete,index)

urlpatterns = [
    url(r'^$',index,name="rmasuk"),
    # url(r'^add',views.add,name="addSatuan"),
    url(r'^save', save, name="saveRmasuk"),
    url(r'^getRmasuk/(?P<id>\d+)$', GetReturJson.as_view(), name="getRmasuk"),
    # url(r'^edit/(?P<id>\d+)$',views.edit,name="editSatuan"),
    # url(r'^update/(?P<id>\d+)$',views.update,name="updateSatuan"),
    url(r'^delete/(?P<id>\d+)$',delete,name="deleteRmasuk"),

]