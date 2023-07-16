from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Achievement, Cat
from .serializers import AchievementSerializer, CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        for cat in data:
            if cat['image']:
                q2 = f"https://kitygramycprac.ddns.net/media/{cat['image']}"
                cat['image'] = q2
        return Response(data)

    def retrieve(self, request, pk=None):
        cat = self.get_object()
        serializer = self.get_serializer(cat)
        data = serializer.data
        if data['image']:
            q1 = f"https://kitygramycprac.ddns.net/media/{data['image']}"
            data['image'] = q1
        return Response(data)


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    pagination_class = None
