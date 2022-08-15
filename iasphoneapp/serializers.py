from rest_framework_json_api import serializers
from django.contrib.auth import authenticate
from iasphoneapp.models import Person

# Person Serializer
class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'surname', 'email')
