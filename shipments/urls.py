from rest_framework import routers
from .api import CountryViewSet, ShipmentViewSet


router = routers.DefaultRouter()
router.register('api/country', CountryViewSet, 'country')
router.register('api/shipment', ShipmentViewSet, 'shipment')

urlpatterns = router.urls
