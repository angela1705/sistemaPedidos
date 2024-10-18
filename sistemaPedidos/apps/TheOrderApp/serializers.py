from rest_framework.serializers import ModelSerializer
from apps.TheOrderApp.models import Producto,Pedido

class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields ='__all__'
class PedidoSerializer(ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'