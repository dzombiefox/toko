from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index,name="kategori"),
    url(r'^add',views.add,name="addKategori"),
    url(r'^save',views.save,name="saveKategori"),
    url(r'^edit/(?P<data>.+)$',views.edit,name="editKategori"),
    url(r'^update/(?P<id>\d+)$',views.update,name="updateKategori"),
    url(r'^delete/(?P<data>.+)$',views.delete,name="deleteKategori"),

]