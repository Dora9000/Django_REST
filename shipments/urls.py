from django.urls import path
from .views import index, create_shipment, \
    get_shipment, get_all_shipment, \
    update_shipment, delete_shipment

from rest_framework import routers
from .api import CountryViewSet, ShipmentViewSet

"""
urlpatterns = [
    path('', index),
    path('add/', create_shipment),
    path('get/', get_shipment),
    path('get_all/', get_all_shipment),
    path('update/', update_shipment),
    path('delete/', delete_shipment),
]
"""


router = routers.DefaultRouter()
router.register('api/country', CountryViewSet, 'country')
router.register('api/shipment', ShipmentViewSet, 'shipment')

urlpatterns = router.urls