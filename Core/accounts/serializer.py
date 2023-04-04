from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'

    def create(self, validated_data):
        user = Account.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user