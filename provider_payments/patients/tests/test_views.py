import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime
import pytz
from ..models import Patient
from ..serializers import PatientSerializer


# initialize the APIClient app
client = Client()

class GetAllPatientsTest(TestCase):
    """ Test module for GET all patients API """

    def setUp(self):
        timezone=pytz.timezone("America/Los_Angeles")

        dob=datetime(2014, 1, 1, 0, 0)
        dob=timezone.localize(dob)
        Patient.objects.create(
            id= '123456789', first_name='Hermes', date_of_birth=dob, social_security_number='555-55-5555', primary_care_physician='Dr. Chrono')

        dob=datetime(1969, 12, 25, 0, 0)
        dob=timezone.localize(dob)
        Patient.objects.create(
            id= '111111111', first_name='Horton', date_of_birth=dob, social_security_number='999-99-9999', primary_care_physician='Dr. Who')

        dob=datetime(1955, 5, 5, 0, 0)
        dob=timezone.localize(dob)
        Patient.objects.create(
            id= '555555555', first_name='Dorothy', date_of_birth=dob, social_security_number='123-45-6789', primary_care_physician='Dr. Oz')

        dob=datetime(1922, 2, 2, 0, 0)
        dob=timezone.localize(dob)
        Patient.objects.create(
            id= '000000000', first_name='Alice', date_of_birth=dob, social_security_number='222-22-2222', primary_care_physician='Dr. Dolittle')


    def test_get_all_patients(self):
        # get API response
        response = client.get(reverse('get_post_patients'))
        # get data from db
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
