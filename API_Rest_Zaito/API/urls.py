from django.urls import path
from API.views.product_views import *
from API.views.image_views import *

urlpatterns = [
    # Ruta para acceder a crear y listar productos
    path('product/', ProductListCreateAPIView.as_view(), name='product_list'),
    # Ruta para obtener, actualizar y eliminar un producto
    path('product/retrieve-update-destroy/<int:pk>', 
        ProductRetrieveUpdateDestroyAPIView.as_view(), name="product_detail"),

    # Ruta para acceder a crear y listar imágenes
    path('image/', ImageListCreateAPIView.as_view(), name="image_list"),
    # Ruta para obtener, actualizar y eliminar una imagen
    path('image/retrieve-update-destroy/<int:pk>', 
        ImageRetrieveUpdateDestroyAPIView.as_view(), name="image_detail"),
]