from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import logout
from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserProfileSerializer
)

# Вью для регистрации пользователя
class UserRegistrationView(generics.CreateAPIView):
	serializer_class = UserRegistrationSerializer
	permission_classes = [permissions.AllowAny]

	def create(self,request,*args,**kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()

		token, created = Token.objects.get_or_create(user=user)

		return Response({
			'user_id': user.id,
			'token': token.key,
			'message': 'Пользователь успешно создан'
		}, status = status.HTTP_201_CREATED)

# Вью для авторизации пользователя
class UserLoginView(APIView):
	permission_classes = [permissions.AllowAny]

	def post(self, request):
		serializer = UserLoginSerializer(data=request.data)
		serializer(raise_exception=True)
		user = serializer.validated_data

		token, created = Token.objects.get_or_create(user=user)

		return Response({
			'user_id': user.id,
			'token': token.key,
			'first_name': user.first_name,
			'last_name': user.last_name,
		})

# Вью для выхода из системы пользователем
class UserLogoutView(APIView):
	permission_classes = [permissions.IsAuthenticated]

	def post(self,request):
		request.user.auth_token.delete()
		logout(request)
		return Response({'message':' Успешный выход из системы '})

# Вью для представления профиля
class UserProfileView(APIView):
	serializer_class = UserProfileSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_objects(self):
		return self.request.user

# Вью деактивации юзера
class UserDeactivateView(APIView):
	permissions_classes = [permissions.IsAuthenticated]

	def post(self,request):
		user = request.user
		user.is_active = False
		user.save()

		user.auth_token.delete()
		logout(request)

		return Response({'message': 'Пользователь деактивирован'})