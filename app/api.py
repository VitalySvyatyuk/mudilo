from rest_framework import views
from rest_framework.response import Response

from .models import Plate
from .utils import clean_p, map_words


class SearchPlates(views.APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request):
        search = request.GET.get('search')
        if not search:
            return Response([])
        plate = clean_p(search.lower())
        plate = map_words(plate)
        if len(plate) < 3:
            return Response([])
        plates = Plate.objects.filter(
            name__contains=plate).values_list('name', 'country')[:6]
        return Response(plates)
