"""toko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth
from django.contrib.auth.decorators import login_required
from main import views as main
urlpatterns = [
    url(r'^kategori/',include('kategori.urls')),
    url(r'^barang/',include('barang.urls')),
    url(r'^suplier/',include('suplier.urls')),
    url(r'^satuan/',include('satuan.urls')),
    url(r'^jumlah/', include('jumlah.urls')),
    url(r'^harga/', include('harga.urls')),
    url(r'^masuk/', include('masuk.urls')),
    url(r'^bmasuk/', include('bmasuk.urls')),
    url(r'^biaya/', include('biaya.urls')),
    url(r'^butang/', include('butang.urls')),
    url(r'^rmasuk/', include('rmasuk.urls')),
    url(r'^jual/', include('jual.urls')),
    url(r'^bjual/', include('bjual.urls')),
    url(r'^rjual/',include('rjual.urls')),
    url(r'^stok/',include('stok.urls')),
    url(r'^ubahstok/',include('ubahstok.urls')),
    url(r'^ekstrakstok/',include('ekstrakstok.urls')),
    url(r'^$', main.index, name='home'),
    url(r'^adminmonon/', admin.site.urls),
    url(r'^users/login/$', auth.login, {'template_name': 'login.html'}, name='login'),
    url(r'^users/logout/$', auth.logout, {'next_page': '/'}, name='logout'),
    url(r'^users/change_password/$', login_required(auth.password_change),
        {'post_change_redirect': '/', 'template_name': 'change_password.html'}, name='change_password'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)