from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Provider
from .serializers import ProviderSerializer
#from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse

@api_view(['GET'])
def get_providers(request):
    # get all providers
    if request.method == 'GET':
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data)
    # insert a new record for a provider
    #if request.method == 'POST':
    #    data = {
    #        'id': request.data.get('id'),
    #        'first_name': request.data.get('first_name'),
    #        'date_of_birth': request.data.get('date_of_birth'),
    #        'social_security_number': request.data.get('social_security_number'),
    #        'primary_care_physician': request.data.get('primary_care_physician')
    #    }
    #    serializer = ProviderSerializer(data=data)
    #    if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data, status=status.HTTP_201_CREATED)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'UPDATE', 'DELETE', 'PUT'])
def get_delete_update_provider(request, pk):
    try:
        provider = Provider.objects.get(pk=pk)
    except Provider.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single provider
    if request.method == 'GET':
        serializer = ProviderSerializer(provider)
        return Response(serializer.data)

     # update details of a single providers
    if request.method == 'PUT':
        serializer = ProviderSerializer(provider, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete a single provider
    elif request.method == 'DELETE':
        provider.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def get_post_providers(request):
    # get all providers
    if request.method == 'GET':
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data)
    # insert a new record for a provider
    elif request.method == 'POST':
        return Response({})

@api_view(['GET', 'POST'])
def get_post_providers(request):
    # get all providers
    if request.method == 'GET':
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data)
    # insert a new record for a provider
    if request.method == 'POST':
        data = {
            'id': request.data.get('id'),
            'first_name': request.data.get('first_name'),
            'date_of_birth': request.data.get('date_of_birth'),
            'social_security_number': request.data.get('social_security_number'),
            'primary_care_physician': request.data.get('primary_care_physician')
        }
        serializer = ProviderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
