from rest_framework import serializers
from enroll.models import Student

class StudentSLR(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'