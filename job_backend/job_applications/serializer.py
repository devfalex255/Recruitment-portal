from rest_framework import serializers
from job_auth.serializer import UserSerializer
from job_applications.models import *

# -------- Job Serializer
class JobSerializer(serializers.ModelSerializer):
    posted_by = UserSerializer(read_only=True)

    class Meta:
        model = Job
        fields = ["primary_key", "unique_id", "title", "description", "posted_by", "created_at"]


# ------ Application Serializer
class ApplicationSerializer(serializers.ModelSerializer):
    applicant = UserSerializer(read_only=True)
    job = serializers.CharField(source="job.title", read_only=True)

    class Meta:
        model = Application
        fields = ["primary_key", "unique_id", "applicant", "job", "status", "created_at"]







        



