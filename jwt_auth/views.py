from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt

from .serializers import UserSerializer
from .populated import PopulatedUserSerializer
from .serializers import EditUserSerializer

User = get_user_model()
class RegisterView(APIView):

    def post(self, request):
        user_to_create = UserSerializer(data=request.data)
        if user_to_create.is_valid():
            user_to_create.save()
            return Response(
                {'message: Registration Succesfull'},
                status=status.HTTP_201_CREATED
            )
        return Response(user_to_create.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class LoginView(APIView):

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user_to_login = User.objects.get(email=email)
        except User.DoesNotExist:
            raise PermissionDenied({'detail': 'Unauthorised'})

        if not user_to_login.check_password(password):
            raise PermissionDenied({'detail': 'Unauthorised'})

        expiry_time = datetime.now() + timedelta(days=7)
        token = jwt.encode(
            {'sub': user_to_login.id, 'exp':  int(expiry_time.strftime('%s'))},
            settings.SECRET_KEY,
            algorithm='HS256'
        )
        return Response(
            {'token': token, 'message': f'Welcome back {user_to_login.username}'}
        )

class ProfileListView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, _request):
        users = User.objects.all()
        serialized_users = PopulatedUserSerializer(users, many=True)
        return Response(serialized_users.data, status=status.HTTP_200_OK)

class ProfileDetailView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, _request, pk):
        try:
            user = User.objects.get(pk=pk)
            serialized_user = PopulatedUserSerializer(user)
            return Response(serialized_user.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            raise NotFound()

    def delete(self, request, pk):
        try:
            user_to_delete = User.objects.get(pk=pk)
            if user_to_delete.id != request.user.id:
                raise PermissionDenied()
            user_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            raise NotFound()

    def put(self, request, pk ):
        user_to_update = User.objects.get(pk=pk)
        request.data['owner'] = request.user.id
        update_user = EditUserSerializer(user_to_update, data=request.data)
        if update_user.is_valid():
            update_user.save()
            return Response(update_user.data, status=status.HTTP_202_ACCEPTED )
        return Response(update_user.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)