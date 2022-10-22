from rest_framework.response import Response
from rest_framework.views import APIView


class BaseHealthCheckAPIView(APIView):
    permission_classes = ()

    @staticmethod
    def get(request):
        return Response(dict(message="Ok"))
