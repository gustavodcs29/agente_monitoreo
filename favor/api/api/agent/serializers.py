from rest_framework import serializers
from .models import *


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model 