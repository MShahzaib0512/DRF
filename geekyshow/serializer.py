from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User
class studentSerializer(serializers.Serializer):
 # class Meta:
 #  model = Student
 #  fields = '__all__'
  name = serializers.CharField(max_length=50)
  age = serializers.IntegerField(default=0)
  city = serializers.CharField(max_length=50)
  
  def create(self, validated_data):
   return Student.objects.create(**validated_data)
class UserSerializer(serializers.Serializer):
 username = serializers.CharField(max_length=50)
 first_name = serializers.CharField(max_length=50)
 last_name= serializers.CharField(max_length=50)
 email = serializers.EmailField()
 password = serializers.CharField(max_length=50)
 
 # field level validations
 
 # def validate_username(self , value):
 #  print(value)
 #  if not value.isalnum():
 #   raise serializers.ValidationError('Username must only contains letter and numbers')
 #  if User.objects.filter(username=value).exists():
 #   raise serializers.ValidationError('User with the username already exists')
 #  return value
 # def validate_email(self , value):
 #  print(value)
 #  if User.objects.filter(email=value).exists():
 #   raise serializers.ValidationError('User with the email already exists')
 #  return value
 
 # object level validation
 def validate(self, data):
  email = data.get('email')
  username = data.get('username')
  
  if not username.isalnum():
   raise serializers.ValidationError('Username must only contains letter and numbers')
  if User.objects.filter(username=username).exists():
   raise serializers.ValidationError('User with the username already exists')
  if User.objects.filter(email=email).exists():
   raise serializers.ValidationError('User with the email already exists')
  return data
 
  """ an other type is only validator we use this type where there is a same validation we used at different serializers such as if i have to use username validation at multiple serializers so i can make the function of that validation and can be use it by user its name in the specific field by validate=[username] 
  
  for example 
  
  def username(value):
    if not username.isalnum():
      raise serializers.ValidationError('Username must only contains letter and numbers')
    if User.objects.filter(username=username).exists():
      raise serializers.ValidationError('User with the username already exists')
      
  class serializer(serializers.Serializer):
   username = serializers.Charfield(max_length = 50 , validators = [username])
  
  """
 
 def create(self, validated_data):
   return User.objects.create_user(**validated_data)
 
# practice serializer for generic api view 

class ItemSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = ['username', 'email', 'password','first_name','last_name' ]
      extra_kwargs = {'password': {'write_only': True}}  # Ensure password is write-only
