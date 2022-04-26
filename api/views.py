from django.contrib.auth import authenticate
from django.middleware import csrf
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import exceptions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from api.serializers import UserPortfolioCreateSerializer, UserPortfolioSerializer, UserRegisterSerializer, \
    CoinSerializer, UserSerializer
from core.models import Portfolio, Coin, User

# worked
from mycryptotracker import settings


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
        print(request.data)
        data = request.data
        portfolio_name = request.data['portfolio']
        token_name = request.data['name']
        price = request.data['buy_price']
        token_price = request.data['coin_price']
        amount = request.data['amount']
        print(amount)
        if amount == 0:
            amount = price / token_price
        portfolio = Portfolio.objects.get(owner_id=request.user.id, name=portfolio_name)
        print(portfolio)
        try:
            token = Coin(name=token_name, buy_price=price, coin_price=token_price, amount=amount)
            token.save()
            portfolio.coins.add(token)
            return Response(data=token.id,status=status.HTTP_201_CREATED)
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


def get_token(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }


class AuthUserInfo(APIView):
    """
    AUTH USER INFORMATION ENDPOINT
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        JWT_auth = JWTAuthentication()
        response = JWT_auth.authenticate(request)
        if response is not None:
            user = User.objects.get(id=response[1]['user_id'])
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class GetUserPortfolios(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        JWT_auth = JWTAuthentication()
        response = JWT_auth.authenticate(request)
        if response is not None:
            user = Portfolio.objects.filter(owner_id=response[1]['user_id'])


# JWT COOKIE STORE
# Работает корректно, но довольно трудно регулировать состояние клиента, и не понятен алгоритм работы при протухании
# При необходимости можно подключить. Маловероятно, что будет использоваться в проекте.

class LoginView(APIView):
    def post(self, request):
        print(request.data)
        data = request.data
        response = Response()
        email = request.data['email']
        password = request.data['password']
        print(email, password)
        user = authenticate(username=email, password=password)
        if user is not None and user.is_active:
            data = get_token(user)
            response.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                value=data["access"],
                expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )
            csrf.get_token(request)
            response.data = {"data": data}
            return response
        else:
            return Response({"Some troubles": "Your account no active or not found"},
                            status=status.HTTP_400_BAD_REQUEST)
