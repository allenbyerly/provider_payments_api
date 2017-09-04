from django.db import models

class Provider(models.Model):
    """
    Provider Model
    Defines the attributes of a provider
    """

    id = models.IntegerField(primary_key=True)
    drg_definition = models.CharField(max_length=255)
    provider_id = models.IntegerField(null=False)
    provider_name = models.CharField(max_length=255)
    provider_street_address = models.CharField(max_length=255)
    provider_city = models.CharField(max_length=255)
    provider_state = models.CharField(max_length=255)
    provider_zipcode = models.CharField(max_length=255)
    hospital_referral_region_description = models.CharField(max_length=255)
    total_discharges = models.IntegerField(null=False)
    average_covered_charges = models.DecimalField(max_digits=100, decimal_places=2, null=False)
    average_total_payments = models.DecimalField(max_digits=100, decimal_places=2, null=False)
    average_medicare_payments = models.DecimalField(max_digits=100, decimal_places=2, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    """
    String for representing the Model object.
    """
    def __str__(self):
        return self.provider_name

    """
    Get Primary Care Physician
    Get the name of the providers primary care physician
    """
    def get_name(self):
        return 'Provider'
        + ' ' + self.first_name
        + ' ' + self.middle_name
        + ' ' + self.last_name
        + ' ' + 'has'
        + ' ' + self. social_security_number
        + ' ' + 'for a SSN'
        + ' ' + 'and'
        + ' ' + self. social_security_number
        + ' ' + 'for a DOB.'

    """
    Get Provider
    Get the providers name, ssn, and
    """
    def get_name(self):
        return 'Provider with SSN:'
        + ' ' + self.social_security_number
        + ' ' + self.middle_name
        + ' ' + self.middle_name
        + ' ' + self.last_name
        + ' ' + 'has'
        + ' ' + self.primary_care_physician
        + ' ' + 'as the primary care physician.'


    """
    Create Provider
    Creare a provider
    """
    def __repr__(self):
        return 'Provider:'
        + ' ' + self.first_name
        + ' ' + self.middle_name
        + ' ' + self.last_name
        + ' ' + 'created.'
