from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Patient
from .serializers import PatientSerializer


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

    # delete a single patient
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single patient
    elif request.method == 'PUT':
        return Response({})


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
