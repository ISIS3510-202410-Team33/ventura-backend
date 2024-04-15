from rest_framework import serializers
from ventura.models import College, College_location, User, User_calification, User_frequency

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'

class College_locationSerializer(serializers.ModelSerializer):
    class Meta:
        model = College_location
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class User_calificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_calification
        fields = '__all__'

class User_frequencySerializer(serializers.ModelSerializer):
    class Meta:
        model = User_frequency
        fields = '__all__'
        