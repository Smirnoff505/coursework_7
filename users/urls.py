from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from users.apps import UsersConfig
from users.views import (
    UserCreateAPIView,
    UserUpdateAPIView,
    UserRetrieveAPIView
)

app_name = UsersConfig.name
urlpatterns = [

    # user
    path('register/', UserCreateAPIView.as_view(),
         name='user-register'),
    path('<int:pk>/update/', UserUpdateAPIView.as_view(),
         name='user-update'),
    path('<int:pk>/profile/', UserRetrieveAPIView.as_view(),
         name='user-profile'),

    # authorization
    path('token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
