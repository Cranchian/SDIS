from app.serializers import ProspectSerializer, UserSerializer
from tenants.utils import tenant_from_request, set_tenant_schema_for_request
from app.models import Prospect
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth import authenticate
from rest_framework import status

class ProspectViewSet(viewsets.ModelViewSet):
    queryset = Prospect.objects.all()
    serializer_class = ProspectSerializer
    
    def get_queryset(self):
        set_tenant_schema_for_request(self.request) #
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)
    
    def destroy(self, request, *args, **kwargs):
        set_tenant_schema_for_request(self.request) #
        prospect = Prospect.objects.get(pk=self.kwargs["pk"])
        if not request.user == prospect.created_by:
            raise PermissionDenied("You can not delete this poll.")
        return super().destroy(request, *args, **kwargs)
    
class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
    
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response(
                {"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST
            )