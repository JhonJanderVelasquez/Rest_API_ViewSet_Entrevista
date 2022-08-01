from pyexpat import model
from tabnanny import verbose
from django.db import models

""" Una imagen solo pudo haberse creado por 1 producto, pero los productos pueden tener muchas imágenes.
 una imagen solo le pertenece a un producto, pero un producto puede tener muchas imágenes asociadas. """

class Producto (models.Model):
    nombre = models.CharField('Nombre del producto', max_length=100, unique=True)
    descripcion = models.TextField('Descripción del producto', max_length=150)
    precio = models.IntegerField('Precio')
    iva = models.IntegerField('Iva')                 # ¿A iva debería realizarse alguna operación con el precio?
    marca = models.CharField('Marca', max_length=25, blank=True, ) 

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"

    def __str__(self):
        return self.nombre

class Imagen (models.Model):
    url = models.CharField('Url de la imagen', max_length=150, blank=True, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Producto')
    """ Llave foránea producto: si se elimina un producto, también se eliminará la imagen.
     Como la imagen solo tiene un producto asociado, y si no existe el producto? Debería eliminarse."""
     # Cuando se ejecute un POST, debería mandarse las imágenes junto con los productos para poder crearlas al mismo tiempo
     # El Delete borra el producto como la imagen.
     

    class Meta:
        verbose_name="Imagen"
        verbose_name_plural="Imágenes"
    
    # def __str__(self):
    #     return self.Url
    
