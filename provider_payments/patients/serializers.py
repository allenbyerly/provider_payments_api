from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('first_name', 'date_of_birth', 'social_security_number', 'primary_care_physician', 'created_at', 'updated_at')
