from .serializers import CompanySerializer, MobileSerializer, RegisterSerializer
from rest_framework import viewsets
from .models import Mobile, Company
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
class MobileViewSet(viewsets.ModelViewSet):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class RegisterView(APIView):
    serializer_class = RegisterSerializer
    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            responce_data =  {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        return Response(responce_data,status=status.HTTP_201_CREATED)