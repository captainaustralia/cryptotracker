from django.urls import path

from api.views import AddPortfolioAPIView, PortfolioListAPIView, RegisterUserAPIView, \
    AddCoinAPIView, DeleteCoinAPIView

urlpatterns = [
    path('addportfolio/', AddPortfolioAPIView.as_view()),
    path('list/', PortfolioListAPIView.as_view()),
    path('register/', RegisterUserAPIView.as_view()),
    path('testadd/', AddCoinAPIView.as_view()),
    path('testdelete/<int:pk>', DeleteCoinAPIView.as_view())
]
