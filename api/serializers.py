from rest_framework import serializers
from core.models import User, Portfolio, Coin


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserPortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ('name', 'buy_price')


class UserRegisterSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.object.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('email', 'username', 'password')


class UserPortfolioCreateSerializer(serializers.ModelSerializer):
    owner = serializers.CurrentUserDefault()
    coins = CoinSerializer(
        many=True
    )

    class Meta:
        model = Portfolio
        fields = ('name', 'coins',)


class UserPortfolioRetrieveSerializer(serializers.ModelSerializer):
    coins = CoinSerializer(
        many=True
    )

    class Meta:
        model = Portfolio
        fields = ('name', 'coins')
