from drf_spectacular.utils import extend_schema
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad
from ads.serializers import AdSerializer


@extend_schema(
    summary="API endpoint that allows you to receive ad by ID.",
)
class AdRetrieveAPIView(RetrieveAPIView):
    """
    API endpoint that allows you to receive ad by ID.
    """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    lookup_field = 'ad_id'
    permission_classes = [IsAuthenticated]
