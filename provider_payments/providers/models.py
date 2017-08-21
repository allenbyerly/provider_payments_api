from django.db import models


class Provider(models.Model):
    """
    Provider Model
    Defines the attributes of a provider
    """
    npi = models.IntegerField()
    name = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    specialty =  models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    """
    Get Name
    Get the name of provider using an npi
    """
    def get_name(self):
        return self.npi + ' belongs to ' + self.name + ' name.'

    """
    Get Specialty
    Get the specialty of provider using an npi
    """
    def get_specialty(self):
        return self.npi + ' belongs to ' + self.specialty + ' specialty.'

    """
    Add Provider
    Add a provider to the DB
    """
    def __repr__(self):
        return self.npi + ' is added.'
