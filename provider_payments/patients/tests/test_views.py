import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime
import pytz
from ..models import Patient
from ..serializers import PatientSerializer
import logging


# initialize the APIClient app
client = Client()

logging.basicConfig()
log = logging.getLogger("LOG")



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

class GetSinglePatientTest(TestCase):
    """ Test module for GET single patient API """

    def setUp(self):
        timezone=pytz.timezone("America/Los_Angeles")

        dob=datetime(2014, 1, 1, 0, 0)
        dob=timezone.localize(dob)
        self.hermes = Patient.objects.create(
            id= '123456789', first_name='Hermes', date_of_birth=dob, social_security_number='555-55-5555', primary_care_physician='Dr. Chrono')

        dob=datetime(1969, 12, 25, 0, 0)
        dob=timezone.localize(dob)
        self.horton = Patient.objects.create(
            id= '111111111', first_name='Horton', date_of_birth=dob, social_security_number='999-99-9999', primary_care_physician='Dr. Who')

        dob=datetime(1955, 5, 5, 0, 0)
        dob=timezone.localize(dob)
        self.dorothy = Patient.objects.create(
            id= '555555555', first_name='Dorothy', date_of_birth=dob, social_security_number='123-45-6789', primary_care_physician='Dr. Oz')

        dob=datetime(1922, 2, 2, 0, 0)
        dob=timezone.localize(dob)
        self.alice = Patient.objects.create(
            id= '000000000', first_name='Alice', date_of_birth=dob, social_security_number='222-22-2222', primary_care_physician='Dr. Dolittle')


    def test_get_valid_single_patient(self):
        response = client.get(
            reverse('get_delete_update_patient', kwargs={'pk': self.horton.pk}))
        patient = Patient.objects.get(pk=self.horton.pk)
        serializer = PatientSerializer(patient)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_patient(self):
        response = client.get(
            reverse('get_delete_update_patient', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewPatientTest(TestCase):
    """ Test module for inserting a new patient """

    def setUp(self):
        timezone=pytz.timezone("America/Los_Angeles")

        dob=datetime(2014, 1, 1, 0, 0)
        dob=timezone.localize(dob)
        self.valid_payload = {
            'id': '111111111',
            'first_name': 'Horton',
            'date_of_birth': dob.isoformat(),
            'social_security_number': '999-99-9999',
            'primary_care_physician': 'Dr. Who'
        }
        log.warning(self.valid_payload)

        dob=datetime(1955, 5, 5, 0, 0)
        dob=timezone.localize(dob)
        self.invalid_payload = {
            'id':  '',
            'first_name': 'Dorothy',
            'date_of_birth': dob.isoformat(),
            'social_security_number': '123-45-6789',
            'primary_care_physician': 'Dr. Oz'
        }
        log.warning(self.invalid_payload)

    def test_create_valid_patient(self):
        response = client.post(
            reverse('get_post_patients'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_patient(self):
        response = client.post(
            reverse('get_post_patients'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSinglePatientTest(TestCase):
    """ Test module for updating an existing patient record """

    def setUp(self):
        timezone=pytz.timezone("America/Los_Angeles")

        dob=datetime(2014, 1, 1, 0, 0)
        dob=timezone.localize(dob)
        self.hermes = Patient.objects.create(
            id= '123456789', first_name='Hermes', date_of_birth=dob, social_security_number='555-55-5555', primary_care_physician='Dr. Chrono')

        dob=datetime(1955, 5, 5, 0, 0)
        dob=timezone.localize(dob)
        self.dorothy = Patient.objects.create(
            id= '555555555', first_name='Dorothy', date_of_birth=dob, social_security_number='123-45-6789', primary_care_physician='Dr. Oz')



        dob=datetime(1955, 5, 5, 0, 0)
        dob=timezone.localize(dob)
        self.valid_payload = {
            'id':  '555555555',
            'first_name': 'Dorothy',
            'date_of_birth': dob.isoformat(),
            'social_security_number': '123-45-6789',
            'primary_care_physician': 'Dr. Oz'
        }
        log.warning(self.valid_payload)

        dob=datetime(2014, 1, 1, 0, 0)
        dob=timezone.localize(dob)
        self.invalid_payload = {
            'id': '',
            'first_name': 'Hermes',
            'date_of_birth': dob.isoformat(),
            'social_security_number': '555-55-5555',
            'primary_care_physician': 'Dr. Chrono'
        }
        log.warning(self.invalid_payload)

    def test_valid_update_patient(self):
        response = client.put(
            reverse('get_delete_update_patient', kwargs={'pk': self.dorothy.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_patient(self):
        response = client.put(
            reverse('get_delete_update_patient', kwargs={'pk': self.hermes.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
