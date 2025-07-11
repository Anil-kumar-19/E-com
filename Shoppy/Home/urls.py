from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from .views import *
from django.conf import *
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)