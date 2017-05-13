from django.conf.urls import url, include
from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(r'cliente', views.ClienteViewSet)
router.register(r'direccion', views.DireccionViewSet)
router.register(r'imagen', views.ImagenViewSet)
router.register(r'position', views.PositionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]
