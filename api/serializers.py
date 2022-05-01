from rest_framework import serializers

from blog.models import Post, Comment
from core.models import User, Portfolio, Coin


# worked
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'is_active', 'is_admin', 'is_staff')


# worked
class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = '__all__'


# worked
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


# worked
class UserPortfolioCreateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Portfolio
        fields = ('name', 'owner')


# worked
class UserPortfolioRetrieveSerializer(serializers.ModelSerializer):
    coins = CoinSerializer(
        many=True
    )

    class Meta:
        model = Portfolio
        fields = ('name', 'coins')


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.IntegerField(
        read_only=True
    )
    owner = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = Comment
        fields = '__all__'
