## third part importation
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken,TokenError
from django.contrib.auth import authenticate

# Custom app importations
from .models import *
from .serializer import *
from  job_utils.permisions import *


## Helper Function: Generate the JWT Token
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


## Regiser API
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


## LogIn API
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        # authenticate the user
        user = authenticate(username=username, password=password)
        if user is None:
            return Response ({
                "error": "Invalid Credentials"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        tokens = get_tokens_for_user(user)
        # store token access_token
        
        return Response ({
            "message": "Login Successful",
            "tokens": tokens,
            "user": UserSerializer(user).data
        }, status=status.HTTP_200_OK)
  

##  API For Logout : Token deleted at the front-end
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]


    def post(self, request):
        refresh_token = request.data.get("refresh")
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            
            return Response({
            "message": "Logout Successful"
            },status=status.HTTP_200_OK)
            

        except TokenError:
            return Response({
            "error": "Invalid/Expired Token"
        },status=status.HTTP_400_BAD_REQUEST)
    


### Change Password API
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        #  check if the old password is correct
        if not request.user.check_password(old_password):
            return Response({
                "error": "Old Password Is Incorrect",
                "status": False
            }, status=status.HTTP_400_BAD_REQUEST)
        
        request.user.set_password(new_password)
        request.user.save()

        return Response (
            {
                "message": "Password Changed Successfully"
            }, status=status.HTTP_200_OK
        )

## Reset Passsword API: Simple password reset using username and new_password
class ResetPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        new_password = request.data.get("new_password")

        ## check if the user exist
        user = User.objects.filter(username=username).first()
        if user is None:
            return Response({
                "status": False,
                "error": "User Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
        
        user.set_password(new_password)
        user.save()

        return Response({
            "message": "Reset Password Successfully"
        },status=status.HTTP_200_OK)
        




