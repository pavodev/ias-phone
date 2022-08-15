from rest_framework_json_api import serializers
from iasphoneapp.models import Person

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'surname', 'email')