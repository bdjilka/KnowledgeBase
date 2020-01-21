from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from pentest_brain.views import PentesterViewSet, SphereViewSet, TagViewSet, CommandViewSet, CommandDocumentView


import config.jwt_refresh

router = routers.DefaultRouter()

router.register(r'users', PentesterViewSet, basename='User')
router.register(r'spheres', SphereViewSet, basename='Sphere')
router.register(r'tags', TagViewSet, basename='Tag')
router.register(r'commands', CommandViewSet, basename='Command')
router.register(r'search', CommandDocumentView, basename='Search')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    url(r'^api/auth/token/login/$', obtain_jwt_token),
    url(r'^api/auth/token/refresh/$', refresh_jwt_token),
]

urlpatterns += staticfiles_urlpatterns()
