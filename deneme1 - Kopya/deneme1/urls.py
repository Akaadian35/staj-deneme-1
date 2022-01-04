from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from mysite.views import index, post_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('posts/<slug:slug>/', post_detail, name='detail')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
