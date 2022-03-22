from rest_framework import serializers
from .models import Country, Shipment


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'

    #def update(self, instance, validated_data):
    #    print(validated_data.keys())
        #if 'user' in validated_data.keys():
        #    user_validated_data = validated_data.pop('user')
        #    user = User.objects.filter(id=instance.user.id).update(**user_validated_data)
    #    return super(ShipmentSerializer, self).update(instance, validated_data)
