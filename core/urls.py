import environ
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

env = environ.Env(DEBUG=(bool, False))

urlpatterns = [
    path(env('DJANGO_ADMIN_URL'), admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Project Standard Admin"
admin.site.site_title = "Project Standard Admin Portal"
admin.site.index_title = "Welcome to the Project Standard Portal"
