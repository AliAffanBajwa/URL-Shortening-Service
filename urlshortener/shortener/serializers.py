from rest_framework import serializers
from .models import ShortURL

class ShortURLSerializer(serializers.ModelSerializer):
    url = serializers.URLField(source='original_url')
    class Meta:
        model = ShortURL
        fields = ['id', 'url', 'short_code', 'created_at', 'updated_at', 'access_count']
        read_only_fields = ['short_code', 'created_at', 'updated_at', 'access_count']
        
    def validate_original_url(self, value):
        if not (value.startswith('http://') or value.startswith('https://')):
            raise serializers.ValidationError("URL must start with http:// or https://")
        return value
    