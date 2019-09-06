from rest_framework import viewsets

from api.models import Category, Journal
from api.serializers import CategorySerializer, JournalSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class JournalViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = JournalSerializer
    queryset = Journal.objects.all()
