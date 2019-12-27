from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from pentest_brain.views import PentesterViewSet, SphereViewSet, TagViewSet, CommandViewSet


router = routers.DefaultRouter()

router.register(r'users', PentesterViewSet, basename='User')
router.register(r'spheres', SphereViewSet, basename='Sphere')
router.register(r'tags', TagViewSet, basename='Tag')
router.register(r'commands', CommandViewSet, basename='Command')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

urlpatterns += staticfiles_urlpatterns()
