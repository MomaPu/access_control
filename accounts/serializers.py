from rest_framework import serializers
from django.contrib.auth import authenticate
from accounts.models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	password_confirm = serializers.CharField(write_only=True)

	class Meta:
		model = CustomUser
		fields = ['email','username','first_name','middle_name','password','password_confirm']

	def validate(self,data):
		if data['password'] != data['password_confirm']:
			raise serializers.ValidationError('Пароли не совпадают')
		return data


	def create(self,validated_data):
		validated_data.pop('password_confirm')
		user = CustomUser.objects.create_user(**validated_data)
		return user

class UserLoginSerializer(serializers.Serializer):
	email = serializers.EmailField()
	password = serializers.CharField(write_only=True)

	def validate(self,data):
		user = authenticate(username=data['email'],
							password=data['password'])
		if not user:
			raise serializers.ValidationError('Неверный email или пароль')
		if not user.is_active:
			raise serializers.ValidationError('Пользователь деактивирован')

		return user

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model=CustomUser
		fields=['email','username','first_name','last_name','middle_name']
		read_only_fields = ['email']