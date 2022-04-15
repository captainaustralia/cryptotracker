from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import exceptions
from api.serializers import UserPortfolioCreateSerializer, UserPortfolioSerializer, UserRegisterSerializer, \
    CoinSerializer
from core.models import Portfolio, Coin


# worked
class CreatePortfolioAPIView(generics.CreateAPIView):
    """
    CREATE USER PORTFOLIO ENDPOINT
    """
    serializer_class = UserPortfolioCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)


# worked
class UserPortfolioAPIView(generics.ListAPIView):
    """
    VIEW USER PORTFOLIOS ENDPOINT
    """
    serializer_class = UserPortfolioSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user_id = self.request.user.id
        return Portfolio.objects.filter(owner_id=user_id)


# worked
class RegisterUserAPIView(generics.CreateAPIView):
    """
    REGISTER USER ENDPOINT
    """
    serializer_class = UserRegisterSerializer


# worked
class AddCoinAPIView(APIView):
    """
    ADD COIN TO PORTFOLIO ENDPOINT
    """
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
        except exceptions.ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# worked , 1 query with 1 join
class DeleteCoinAPIView(generics.DestroyAPIView):
    """
    DELETE CURRENT COIN FROM PORTFOLIO
    """
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
        except exceptions.ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
