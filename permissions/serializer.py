from rest_framework import serializers
from django.contrib.auth.models import User

class ItemSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = ['username', 'email', 'password','first_name','last_name' ]
      extra_kwargs = {'password': {'write_only': True}}  # Ensure password is write-only
