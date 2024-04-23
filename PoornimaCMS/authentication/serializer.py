from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token

from courses.models import Subject,Semester,Branch
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    is_faculty =  serializers.BooleanField
    
    subjects = serializers.PrimaryKeyRelatedField(many=True, queryset=Subject.objects.all(), required=False)
    branch = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all(), required=False)
    semester = serializers.PrimaryKeyRelatedField(queryset=Semester.objects.all(), required=False)
    profile_picture = serializers.ImageField(allow_null=True, required=False)

    class Meta:
        model = CustomUser
        fields = ["id", "email", "password", "confirm_password","name","contact_info","registration_no","subjects","branch","semester","is_faculty", 'profile_picture']
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Passwords do not match")
        validate_password(data["password"])
        data.pop("confirm_password", None)
        return data
        
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)
    
    
    
    
