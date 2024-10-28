from rest_framework import serializers
from .models import *

class Web_designSerializers(serializers.ModelSerializer):
    class Meta:
        models = WebDesignModel
        fields = "__all__"