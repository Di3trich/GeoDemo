from django.conf.urls import url, include
from rest_framework import routers
from core import views
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'cliente', views.ClienteViewSet, base_name='cliente')
router.register(r'direccion', views.DireccionViewSet, base_name='direccion')
router.register(r'imagen', views.ImagenViewSet, base_name='imagen')
router.register(r'position', views.PositionViewSet, base_name='position')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include_docs_urls(title='Api Docs'))
]
