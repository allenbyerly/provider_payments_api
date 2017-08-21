from django.test import TestCase
from datetime import datetime
import pytz
from ..models import Patient


class PatientTest(TestCase):
    """ Test module for Patient model """

    def setUp(self):
        dob=datetime(2014, 1, 1, 0, 0)
        timezone=pytz.timezone("America/Los_Angeles")
        dob=timezone.localize(dob)

        Patient.objects.create(
            id= '123456789', first_name='Hermes', date_of_birth=dob, social_security_number='555-55-5555', primary_care_physician='Dr. Chrono')
        Patient.objects.create(
            id= '555555555', first_name='Horton', date_of_birth=dob, social_security_number='4123-45-6789', primary_care_physician='Dr. Who')

    def test_patient_primary_care_physician(self):
        patient_hermes = Patient.objects.get(first_name='Hermes')
        patient_horton = Patient.objects.get(first_name='Horton')
        self.assertEqual(
            patient_hermes.get_primary_care_physician(), "Patient Hermes has Dr. Chrono as the primary care physician.")
        self.assertEqual(
            patient_horton.get_primary_care_physician(), "Patient Horton has Dr. Who as the primary care physician.")
