from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes, api_view
from rest_framework import permissions
from .serializer import PastelesSerializer
from .models import Pasteles


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def pastel_api_view(request):
    if request.method == 'GET':
        pasteles = Pasteles.objects.all()
        pasteles_serializer = PastelesSerializer(pasteles, many=True)
        return Response({'status': 'ok', 'pasteles': pasteles_serializer.data})
    elif request.method == 'POST':
        pastel_serializer = PastelesSerializer(data=request.data)
        if pastel_serializer.is_valid():
            pastel_serializer.save()
            return Response(pastel_serializer.data)
        return Response(pastel_serializer.errors)


@api_view(['GET'])
def pastel_phk_api_view(request, pk=None):
    if request.method == 'GET':
        pastel = Pasteles.objects.filter(id=pk).first()
        pastel_serializer = PastelesSerializer(pastel)
        return Response(pastel_serializer.data)

    # def get(self, request):
    #     respuesta = [1, 2, 3, 4]
    #     return Response({'status': 'ok', 'message': 'hello', 'respuesta': respuesta})
