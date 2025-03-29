from rest_framework import serializers
from postoffice.models import Letters, Parcels


class LetterSerializer(serializers.ModelSerializer):
    """ Letter model serializer """
    
    class Meta:
        model = Letters
        fields = "__all__"


class ParcelSerializer(serializers.ModelSerializer):
    """ Parcel model serializer """
    
    class Meta:
        model = Parcels
        fields = "__all__"
