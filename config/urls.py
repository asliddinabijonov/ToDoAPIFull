from django.contrib import admin
from django.conf.urls.i18n import set_language
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from mainApp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('set_language/', set_language, name='set_language'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('plans/', PlansAPIView.as_view()),
    path('plan/<int:pk>/', PlanAPIView.as_view()),
    path('plan/<int:pk>/update/', PlanUpdateAPIView.as_view()),
    path('plan/<int:pk>/delete/', PlanDeleteAPIView .as_view()),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
