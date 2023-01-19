from django.urls import path,include
from rest_framework import routers
from api_app import views

router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'groups',views.GroupViewset)

urlpatterns = [
    path("", include(router.urls)),
    path("api_auth/"),include('rest_framework.urls',namespace='rest_framework')
]
