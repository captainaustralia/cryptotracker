from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import UserPortfolioCreateSerializer, UserPortfolioSerializer, UserPortfolioRetrieveSerializer, \
    UserRegisterSerializer, CoinSerializer
from core.models import Portfolio, User, Coin


class AddPortfolioAPIView(generics.ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = UserPortfolioCreateSerializer
    permission_classes = (AllowAny,)


class PortfolioListAPIView(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = UserPortfolioSerializer


class RegisterUserAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer


# worked
class AddCoinAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        data = request.data
        token_name = request.data['name']
        price = request.data['buy_price']
        token_price = request.data['coin_price']
        amount = request.data['amount']
        portfolio = Portfolio.objects.get(owner_id=request.user.id)
        print(portfolio)
        try:
            token = Coin(name=token_name, buy_price=price, coin_price=token_price, amount=amount)
            token.save()
            portfolio.coins.add(token)
            return Response(status=status.HTTP_201_CREATED)
        except EOFError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# worked , 1 query with 1 join
class DeleteCoinAPIView(generics.DestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = CoinSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def destroy(self, request, *args, **kwargs):
        try:
            coin = Coin.objects.get(id=kwargs['pk'])
            if Portfolio.objects.prefetch_related('coins').filter(coins__id=kwargs['pk'], owner__id=request.user.id):
                coin.delete()
                return Response(status=status.HTTP_202_ACCEPTED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
