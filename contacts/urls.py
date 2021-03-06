from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('app.urls')),
                  path('', include('django.contrib.auth.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# customising dmin text

admin.site.site_header = 'Contacts'
admin.site.index_title = 'George is Super Programmer'
admin.site.site_title = 'Super Title'
