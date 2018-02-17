from rest_framework import serializers

from .models import BucketList

class BucketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BucketList
        fields = ('id', 'name', 'created_at', 'modified_at')
        read_only_fields = ('created_at', 'modified_at')
        