from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import UserSerializer, LoanSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from .models import Loan

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'admin': user.is_staff,
            'username': user.username
        })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes_by_action = {'create': [IsAuthenticated],
                                    'partial_update': [IsAdminUser],
                                    'list': [IsAuthenticated],
                                    'list_pending': [IsAdminUser],
                                    }

    def list(self, request, *args, **kwargs):
        user = self.request.user
        loans = Loan.objects.filter(user=user.pk)
        serializer = self.serializer_class(loans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def list_pending(self, request, pk=None):
        loans = Loan.objects.filter(status='pending')
        serializer = self.serializer_class(loans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, pk=None):
        amount = request.data['amount']
        term = request.data['term']
        loan = Loan.objects.create(user=request.user, amount=amount, term=term)
        loan.save()

        serializer = self.serializer_class(loan)
        response = {'message': 'Loan has been successfully requested',
                    'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]    
