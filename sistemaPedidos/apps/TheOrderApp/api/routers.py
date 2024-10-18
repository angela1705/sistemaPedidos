from rest_framework.routers import DefaultRouter
from.views import PedidoViewSet, ProductoViewSet
 
router=DefaultRouter()
router.register(prefix='producto', viewset=ProductoViewSet)
router.register(prefix='pedido', viewset=PedidoViewSet)
