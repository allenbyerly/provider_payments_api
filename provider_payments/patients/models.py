from django.db import models


class Patient(models.Model):
    """
    Puppy Model
    Defines the attributes of a puppy
    """
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    social_security_number = models.CharField(max_length=255)
    date_of_birth = models.DateTimeField()
    gender = models.CharField(max_length=255)
    ethnicity = models.CharField(max_length=255)
    preferred_language = models.CharField(max_length=255)
    race = models.CharField(max_length=255)
    doctor = models.IntegerField(null=True)
    primary_care_physician = models.CharField(max_length=255)
    chart_id = models.CharField(max_length=255)
    patient_payment_profile = models.CharField(max_length=255)
    default_pharmacy = models.CharField(max_length=255)
    responsible_party_name  = models.CharField(max_length=255)
    responsible_party_relation = models.CharField(max_length=255)
    responsible_party_phone = models.CharField(max_length=255)
    responsible_party_email = models.CharField(max_length=255)
    offices = models.CharField(max_length=255)
    since = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    email =  models.CharField(max_length=255)
    home_phone =  models.CharField(max_length=255)
    cell_phone =  models.CharField(max_length=255)
    emergency_contact_name = models.CharField(max_length=255)
    emergency_contact_phone = models.CharField(max_length=255)
    emergency_contact_relation =  models.CharField(max_length=255)
    employer =  models.CharField(max_length=255)
    employer_address = models.CharField(max_length=255)
    employer_city = models.CharField(max_length=255)
    employer_state = models.CharField(max_length=255)
    employer_zip_code = models.CharField(max_length=255)
    emergency_contact_name = models.CharField(max_length=255)
    emergency_contact_phone = models.CharField(max_length=255)
    emergency_contact_relation =  models.CharField(max_length=255)
    employer =  models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    """
    String for representing the Model object.
    """
    def __str__(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name

    """
    Get Primary Care Physician
    Get the name of the patients primary care physician
    """
    def get_details(self):
        return 'Patient',
        + ' ' + self.first_name,
        + ' ' + self.middle_name,
        + ' ' + self.last_name,
        + ' ' + 'has',
        + ' ' + self.social_security_number,
        + ' ' + 'for a SSN',
        + ' ' + 'and',
        + ' ' + self.date_of_birth,
        + ' ' + 'for a DOB.'

    """
    Get Patient
    Get the patients name, ssn, and
    """
    def get_primary_care_physician(self):
        return 'Patient' + ' ' + self.first_name + ' ' + 'has' + ' ' + self.primary_care_physician + ' ' + 'as the primary care physician.'


    """
    Create Patient
    Creare a patient
    """
    def __repr__(self):
        return 'Patient:'
        + ' ' + self.first_name
        + ' ' + self.middle_name
        + ' ' + self.last_name
        + ' ' + 'created.'
