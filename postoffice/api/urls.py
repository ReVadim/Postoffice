from django.urls import path, include
from postoffice.api import api_views
from rest_framework import routers

app_name = 'postofice_api'
router = routers.DefaultRouter()
router.register('letters', api_views.LetterViewSet)
router.register('parcels', api_views.ParcelViewSet)


urlpatterns = [

    path('', include(router.urls)),
]
