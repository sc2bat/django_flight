from rest_framework import generics
from .models import Admins
from .serializers import YourModelSerializer

class YourModelListAPIView(generics.ListAPIView):
    queryset = Admins.objects.all()
    serializer_class = YourModelSerializer