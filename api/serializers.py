from rest_framework import serializers
from core.models import User, Portfolio, Coin


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'is_active', 'is_admin', 'is_staff')


class CoinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coin
        fields = '__all__'


class UserPortfolioSerializer(serializers.ModelSerializer):
    coins = CoinSerializer(read_only=True, many=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Portfolio
        exclude = ('id',)


# worked
class UserRegisterSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('email', 'username', 'password')


class UserPortfolioCreateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Portfolio
        fields = ('name', 'owner')


class UserPortfolioRetrieveSerializer(serializers.ModelSerializer):
    coins = CoinSerializer(
        many=True
    )

    class Meta:
        model = Portfolio
        fields = ('name', 'coins')
