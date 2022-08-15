from django.shortcuts import render
from iasphoneapp.models import Person
from iasphoneapp.serializers import PersonSerializer
from rest_framework import viewsets

from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response

from . import serializers

# Create your views here.

class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = serializers.LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
