from rest_framework.routers import DefaultRouter
from API.views.product_views import ProductViewSet
from API.views.image_views import ImageViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'images', ImageViewSet, basename='images')

urlpatterns = router.urls