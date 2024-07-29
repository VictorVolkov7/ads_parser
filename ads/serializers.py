from rest_framework import serializers

from ads.models import Ad


class AdSerializer(serializers.ModelSerializer):
    """
    Serializer for ad model.
    """
    class Meta:
        model = Ad
        fields: tuple = ('title', 'ad_id', 'author', 'views', 'position')
