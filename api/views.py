from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework import generics, views, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import get_list_or_404
from django.db.models import Q
from .serializers import *

class SignupAPIView(generics.CreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    
    serializer_class = UserRegistrationSerializer


class BlockDetailAPIView(generics.RetrieveAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [AllowAny]
    
    queryset = Block.objects.all()
    serializer_class = BlocksDetailSerializer
    lookup_field = 'block_id'



class TransactionDetailAPIView(generics.RetrieveAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [AllowAny]
    
    queryset = Transactions.objects.all()
    serializer_class = TransactionsDetailSerializer
    lookup_field = 'txID'


class AddressAPIView(views.APIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [AllowAny]
    
    
    def get(self, request, address, *args, **kwargs):
        
        queryset = get_list_or_404(Transactions, (Q(owner_address=address) | Q(to_address=address)))
        serializer = TransactionsDetailSerializer(queryset, many=True)  

        return Response(serializer.data, status=status.HTTP_200_OK)
