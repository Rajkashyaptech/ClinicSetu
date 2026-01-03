from rest_framework.views import APIView
from rest_framework.response import Response

from common.api_permissions import IsDoctor
from apps.medicines.models import Medicine
from .serializers import MedicineAutocompleteSerializer


class MedicineAutocompleteAPI(APIView):
    permission_classes = [IsDoctor]

    def get(self, request):
        query = request.query_params.get("q", "").strip()

        if not query:
            return Response([])
        
        qs = Medicine.objects.filter(
            name__istartswith=query
        ).order_by("name")[:10]

        return Response(
            MedicineAutocompleteSerializer(qs, many=True).data
        )
