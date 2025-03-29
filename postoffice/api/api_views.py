from rest_framework import viewsets
from postoffice.models import Letters, Parcels
from postoffice.api.serializers import LetterSerializer, ParcelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from postoffice.api.classes import Paginator


class LetterViewSet(viewsets.ModelViewSet):
    """ Letters ViewSet """
    queryset = Letters.objects.all()
    serializer_class = LetterSerializer
    http_method_names = ['get', 'post']
    pagination_class = Paginator
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['letter_type', 'letter_weight']
    filterset_fields = ['letter_type', 'receive_postal_code']


class ParcelViewSet(viewsets.ModelViewSet):
    """ Parcels ViewSet """
    queryset = Parcels.objects.all()
    serializer_class = ParcelSerializer
    http_method_names = ['get', 'post', 'put']
    pagination_class = Paginator
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['parcel_type']
    filterset_fields = ['parcel_type', 'receive_postal_code']