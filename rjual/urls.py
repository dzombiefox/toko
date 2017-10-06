from django.conf.urls import url
from . import views
from views import (save,delete,GetRjualJson,index)

urlpatterns = [
    url(r'^$',index,name="rjual"),
    # url(r'^add',views.add,name="addSatuan"),
    url(r'^save', save, name="saveRjual"),
    url(r'^getRjual/(?P<id>\d+)$', GetRjualJson.as_view(), name="getRjual"),
    # # url(r'^edit/(?P<id>\d+)$',views.edit,name="editSatuan"),
    # # url(r'^update/(?P<id>\d+)$',views.update,name="updateSatuan"),
    url(r'^delete/(?P<id>\d+)$',delete,name="deleteRjual"),

]