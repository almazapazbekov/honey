"""honey_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken.views import obtain_auth_token

from account.views import UserCreateAPIView, UserRetrieveUpdateDestroyAPIView

schema_view = get_schema_view(
    openapi.Info(
        title="МЁД",
        default_version='v0.1',
        description="API Для магазина по продаже мёда",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="___"),

        license=openapi.License(name="Лицензии нет"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('auth/', include('rest_framework.urls')),
                  path('account/token/', obtain_auth_token),
                  path('shop/', include('shop.urls')),
                  path('shop/order/', include('order.urls')),
                  path('register/', UserCreateAPIView.as_view()),
                  path('user/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view()),

                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_ui'),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc_ui'),
                  path('json_doc/', schema_view.without_ui(cache_timeout=0), name='json_doc'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
