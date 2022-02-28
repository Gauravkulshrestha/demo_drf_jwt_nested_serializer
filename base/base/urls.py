from django.contrib import admin
from django.urls import path, include
from api.views import MobileViewSet 
from rest_framework.routers import DefaultRouter
from api.views import CompanyViewSet, MobileViewSet, RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'mobileapi', MobileViewSet, basename='mobile')
router.register(r'companyapi', CompanyViewSet, basename='company')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='register'),
]