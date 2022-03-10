from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from .settings import MEDIA_ROOT,MEDIA_URL
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('rating/', include('rating.urls')),
    path('hostel/', include('hostel.urls')),   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
