from django.conf.urls import url, include
from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(r'cliente', views.ClienteViewSet, base_name='cliente')
router.register(r'direccion', views.DireccionViewSet, base_name='direccion')
router.register(r'imagen', views.ImagenViewSet, base_name='imagen')
router.register(r'position', views.PositionViewSet, base_name='position')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]
