from rest_framework import generics
# Trae los modelos
from API.models import Imagen
# Trae el serializador para producto
from API.serializers.general_serializers import ImageSerializer
# Status y Response 
from rest_framework import status
from rest_framework.response import Response


# Listar y crear imágenes
class ImageListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ImageSerializer

    # Sobreescribiendo método post de la clase
    def post (self, request): 
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Imagen creada exitosamente'}, status= status.HTTP_201_CREATED)
        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return Imagen.objects.all()



# Clase para obtener un objeto, actualizar y eliminar
class ImageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter()
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk).first()

    # Devuelve los datos de la instancia       
    def patch(self, request, pk=None):
        if self.get_queryset(pk):
            Image_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(Image_serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'No existe una imagen con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

    # Actualizar registro de imagen
    def put(self, request, pk=None):
        if self.get_queryset(pk):
            Image_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if Image_serializer.is_valid():
                Image_serializer.save()
                return Response({
                    "message": "Imagen actualizada", 
                    'response': Image_serializer.data
            }, status=status.HTTP_200_OK)
        return Response({'error':'No existe una imagen con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

    # Este método sobreescribe el delete, no es necesario porque la clase lo ejecuta por default, 
    # pero es para tener un mayor control. 
    def delete(self, request, pk=None):
        image = self.get_queryset().filter(id=pk).first()
        if image:
            image.delete()
            return Response({'message':'Imagen eliminada exitosamente'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe una imagen con estos datos...'}, status=status.HTTP_400_BAD_REQUEST)

