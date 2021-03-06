from rest_framework import serializers
from core.models import TBase

class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_blank=False, max_length=255)
    score = serializers.DecimalField(max_digits=9, decimal_places=4)

class TBaseSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, allow_blank=False, max_length=255)
    score = serializers.DecimalField(max_digits=9, decimal_places=4)
    people = PersonSerializer(many=True)
    created_at = serializers.DateTimeField(allow_null=True, required=False, read_only=True)
    updated_at = serializers.DateTimeField(allow_null=True, required=False, read_only=True)

    class Meta:
        model = TBase
        fields = ("name", "score", "people", "created_at", "updated_at")
        read_only_fields = ("created_at", "update_at")

    def create(self, validated_data):
        people = validated_data.pop('people')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album, **track_data)
        return album

