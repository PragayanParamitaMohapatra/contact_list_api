from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=['id','country','first_name','last_name','phone_number','contact_picture','is_favourite']