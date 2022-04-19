from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from api.views import CreatePortfolioAPIView, UserPortfolioAPIView, RegisterUserAPIView, \
    AddCoinAPIView, DeleteCoinAPIView, LoginView

urlpatterns = [
    path('addportfolio/', CreatePortfolioAPIView.as_view(), name='create_portfolio'),
    path('portfolio/', UserPortfolioAPIView.as_view(), name='portfolio'),
    path('register/', RegisterUserAPIView.as_view(), name='register'),
    path('addtoken/', AddCoinAPIView.as_view(), name='add_coin'),
    path('deletetoken/<int:pk>', DeleteCoinAPIView.as_view(), name='delete_token'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify')
    # path('spec_auth/', LoginView.as_view(), name='login')  # cookies auth
]
