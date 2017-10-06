from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^view/(?P<data>.+)$',views.index,name="butang"),
    url(r'^save',views.save,name="saveHutang"),
    url(r'^data', views.data, name="databutang"),
    url(r'^delete/(?P<id>\d+)$',views.delete,name="deleteButang"),
    url(r'^print/(?P<id>\d+)$',views.prints,name="printButang"),

]