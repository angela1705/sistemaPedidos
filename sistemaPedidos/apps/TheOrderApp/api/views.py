from rest_framework.viewsets import ModelViewSet
from apps.TheOrderApp.models import Producto,Pedido
from apps.TheOrderApp.serializers import ProductoSerializer, PedidoSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import Mipermiso

class ProductoViewSet(ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class PedidoViewSet(ModelViewSet):
    permission_classes =[Mipermiso]
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    http_method_names = ['get','post']