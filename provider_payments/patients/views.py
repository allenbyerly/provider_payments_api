from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Patient
from .serializers import PatientSerializer
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')

@api_view(['GET', 'UPDATE', 'DELETE', 'PUT'])
def get_delete_update_patient(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single patient
    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

     # update details of a single patients
    if request.method == 'PUT':
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete a single patient
    elif request.method == 'DELETE':
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def get_post_patients(request):
    # get all patients
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    # insert a new record for a patient
    elif request.method == 'POST':
        return Response({})

@api_view(['GET', 'POST'])
def get_post_patients(request):
    # get all patients
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    # insert a new record for a patient
    if request.method == 'POST':
        data = {
            'id': request.data.get('id'),
            'first_name': request.data.get('first_name'),
            'date_of_birth': request.data.get('date_of_birth'),
            'social_security_number': request.data.get('social_security_number'),
            'primary_care_physician': request.data.get('primary_care_physician')
        }
        serializer = PatientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
