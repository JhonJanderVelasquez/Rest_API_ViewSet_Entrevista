from rest_framework import generics
# Trae los modelos
from API.models import Producto
# Trae el serializador para producto
from API.serializers.general_serializers import ProductSerializer

from rest_framework import status
from rest_framework.response import Response

# Crear y listar productos
class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    # Sobreescribiendo método post de la clase
    def post (self, request): 
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response ({'message': 'Producto creado exitosamente'}, status= status.HTTP_201_CREATED)
        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return Producto.objects.all()



# Clase APIView para obtener un objeto, actualizar y eliminar
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter()
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk).first()

    # Devuelve los datos de la instancia para realizar update.        
    def patch(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un producto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

    # Actualiza registro con un id ingresado por url.
    def put(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response({
                    "message": "Producto actualizado", 
                    'response': product_serializer.data
                }, status=status.HTTP_200_OK)
        return Response({'error':'No existe un producto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)


    # Este método sobreescribe el delete, no es necesario, pero se puede tener un mayor control. 
    def delete(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.delete()
            return Response({'message':'Producto eliminado exitosamente'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un producto con estos datos...'}, status=status.HTTP_400_BAD_REQUEST)

    