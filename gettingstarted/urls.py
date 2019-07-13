from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views
import caixa_racional.views as cr

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path('api/', cr.ApiRoot.as_view(), name=cr.ApiRoot.name),
    path('api/temperaturas/', cr.TemperaturaList.as_view(), name=cr.TemperaturaList.name),
    path('api/temperaturas/<int:pk>', cr.TemperaturaDetail.as_view(), name=cr.TemperaturaDetail.name),
    path('api/base-de-dados/', cr.BaseDeDadosList.as_view(), name=cr.BaseDeDadosList.name),
    path('api/base-de-dados/<int:pk>', cr.BaseDeDadosDetail.as_view(), name=cr.BaseDeDadosDetail.name),
]
