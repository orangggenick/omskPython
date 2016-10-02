from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from AdminOmsk.views import home, press

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'press', press, name='press'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
