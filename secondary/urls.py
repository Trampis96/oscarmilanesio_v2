from django.urls import path
from django.conf import settings
from .views import HomeView,GalleryView,AboutUsView

urlpatterns = [
    path('',HomeView,name='inicio'),
    path('trabajos/',GalleryView.as_view(),name='trabajos'),
    path('contacto/',AboutUsView,name='contacto'),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
