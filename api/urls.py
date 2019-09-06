from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import CategoryViewSet, JournalViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'journals', JournalViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
