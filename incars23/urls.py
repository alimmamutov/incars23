"""
URL configuration for incars23 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from incars23.settings import DEBUG
from main import views
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from incars23 import settings
from django.contrib.sitemaps.views import sitemap
from .sitemaps import CarSitemap, StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
    # "cars": CarSitemap
}


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]


if DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
