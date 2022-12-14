from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']
    
    def create(self, validated_data):
        user=User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user





class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name','roll','city']
    
 
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
      instance.name=validated_data.get('name',instance.name)
      instance.roll=validated_data.get('roll',instance.roll)
      instance.city=validated_data.get('city',instance.city)
      instance.save()
      return instance
     

    
    
    
      