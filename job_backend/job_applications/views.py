## third part importation
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

## other app imports
from .models import *
from .serializer import *
from job_utils.permisions import *


# create: post, update:put(id), delete:delete(id), get:get

## ---- Create JOB API
#  -----ADMIN: Can Create the Job
class CreateJobView(APIView):
    permission_classes = [IsAuthenticated, IsAdminRole]

    def post(self, request):
        title = request.data.get("title")
        description = request.data.get("description")

        ## Input Validation
        if not title or not description:
            return Response ({
                "status": False,
                "error": "Bad Request"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        ## check if the Job exist
        if Job.objects.filter(title=title).exists():
            return Response ({
                "status": False,
                "error": "This Job Already Exists"
            }, status=status.HTTP_409_CONFLICT)

        job = Job.objects.create(
            title = title,
            description=description,
            posted_by=request.user,
        )

        return Response({
            "status": True,
            "message": "Job Created Successfully",
            "data": JobSerializer(job).data
        },
        status=status.HTTP_201_CREATED)


# ------ Update Job View -----------
class UpdateJobView(APIView):
    permission_classes = [IsAuthenticated, IsAdminRole]

    def put(self, request, id):
        title = request.data.get("title")
        description = request.data.get("description")

        ## Input Validation
        if not title or not description:
            return Response ({
                "status": False,
                "error": "Bad Request"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        ## check if the Job exist
        job = Job.objects.filter(primary_key=id).first()
        if Job is None:
            return Response({
            "status": False,
            "message": "Job Does Not Exist"
        },
        status=status.HTTP_404_NOT_FOUND)
        # update the fields   
        job.title=title
        job.description=description
        job.save()
    
        return Response({
            "status": True,
            "message": "Job Updated Successfully",
            "data": JobSerializer(job).data
        },
        status=status.HTTP_200_OK)



# ------- Delete Job ---------------
class DeleteJobView(APIView):
    permission_classes = [IsAuthenticated, IsAdminRole]

    def delete(self, request, id):

        # check if the job exist
        job = Job.objects.filter(primary_key=id).first()
        if job is None:
            return Response({
            "status": False,
            "message": "Job Does Not Exist"
        },
        status=status.HTTP_404_NOT_FOUND)

        # soft delete
        job.is_active=False
        job.save()

        return Response({
            "status": True,
            "message": "Job Deleted Successfully",
            "data": JobSerializer(job).data
        }, status=status.HTTP_200_OK)

# ----------------------------------
# Delete a Job API (Admin Only)
# ----------------------------------
class ViewJobDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        jobs = Job.objects.filter(is_active=True).all()

        return Response({
            "status": True,
            "message": "Operation Successfully",
            "data": JobSerializer(jobs, many=True).data
        }, status=status.HTTP_200_OK
        )



# -----------------------------
# Apply to a job (Candidate only)
# -----------------------------
class ApplyJobView(APIView):
    permission_classes = [IsAuthenticated, IsCandidateRole]

    def post(self, request):
        job_id = request.data.get("job_id")

        # check if the job exist
        job = Job.objects.filter(primary_key=job_id, is_active=True).first()
        if job is None:
            return Response({
                "status": False,
                "message": "Job Does Not Exist"
            }, status=status.HTTP_404_NOT_FOUND)
        
        # prevent apply twice
        if Application.objects.filter(job=job, applicant=request.user).exists():
            return Response({"error": "Already Applied to This Job"}, status=status.HTTP_409_CONFLICT)

        application = Application.objects.create(job=job, applicant=request.user)
        return Response({
            "status": True,
            "message": "Operation Successfully",
            "data": ApplicationSerializer(application).data
        }, status=status.HTTP_201_CREATED) 
    

# -----------------------------
# Candidate: Veiw their Application
# Admin: View all Applications
# -----------------------------
class ApplicationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role == "ADMIN":
            applications = Application.objects.filter(is_active=True).all()

        if request.user.role == "CANDIDATE":
            applications = Application.objects.filter(is_active=True, applicant=request.user).all()

        return Response({
            "status": True,
            "message": "Operation Successfully",
            "data": ApplicationSerializer(applications, many=True).data
        }, status=status.HTTP_200_OK)

    

# --------------------------------
# Admin: Update application status
# --------------------------------
class ApplicationStatusUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminRole]

    def put(self, request, id):
        status_value = request.data.get("status")

        # Input validations
        if status_value not in ["PENDIND", "APPROVED", "REJECTED"]:
            return Response({
                "status": False,
                "message": "Status Does Not Exist"
            }, status=status.HTTP_404_NOT_FOUND)
        
        try:
            application = Application.objects.filter(primary_key=id).first()
        
        except Application.DoesNotExist:
            return  Response({"error": "Application not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        application.status= status_value
        application.save()

        return Response({
            "message": "Status Updated Successfully",
            "application": ApplicationSerializer(application).data
            },
            status=201
            )
    

