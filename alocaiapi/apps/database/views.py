from django.shortcuts import get_object_or_404
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from ...helpers.renderers import RequestJSONRenderer


class DatabaseConnectionApiView(generics.GenericAPIView):
    # renderer_classes = (RequestJSONRenderer,)

    def get(self, request):
        pass
