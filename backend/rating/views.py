from rest_framework import viewsets
from .serializers import RatingSerializer
from .models import Rating

# Create your views here.


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all().order_by('user')
    serializer_class = RatingSerializer
