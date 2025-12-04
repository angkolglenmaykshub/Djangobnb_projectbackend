from rest_framework import serializers


from .models import Property


from useraccount.serializers import UserDetailSerializer






class PropertiesListSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()


    def get_image_url(self, obj):
        return obj.image_url()


    class Meta:
        model = Property
        fields = (
            'id',
            'title',
            'price_per_night',
            'image_url',
        )


class PropertiesDetailSerializer(serializers.ModelSerializer):
    landlord = UserDetailSerializer(read_only=True, many=False)
    image_url = serializers.SerializerMethodField()


    def get_image_url(self, obj):
        return obj.image_url()


    class Meta:
        model = Property
        fields = (
            'id',
            'title',
            'description',
            'price_per_night',
            'image_url',
            'bedrooms',
            'bathrooms',
            'guests',
            'landlord'
        )


