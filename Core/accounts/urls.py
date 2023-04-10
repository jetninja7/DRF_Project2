from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('login/', views.login, name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
