from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import GameSerializer
from ...helpers.constants import SUCCESS_MESSAGE
from ...helpers.renderers import RequestJSONRenderer


class GamesApiView(generics.GenericAPIView):
    """ Class to add order items """
    renderer_classes = (RequestJSONRenderer,)
    serializer_class = GameSerializer

    def post(self, request):
        """ Method to add a new game """
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return_message = {
                'message':
                SUCCESS_MESSAGE.format("The game has been created"),
                "data": serializer.data
            }
            return Response(return_message, status=status.HTTP_201_CREATED)
        except Exception as e:
            return_message = {
                'message': str(e)
            }
            return Response(return_message, status=status.HTTP_400_BAD_REQUEST)
