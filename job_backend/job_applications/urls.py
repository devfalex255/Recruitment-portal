from django.urls import path
from .views import *







# define urls patterns
urlpatterns = [
    path("create/", CreateJobView.as_view()),
    path("update/<int:id>/", UpdateJobView.as_view()),
    path("delete/<int:id>/", DeleteJobView.as_view()),
    path("list/", ViewJobDetails.as_view()),

    ## applications
    path("apply/", ApplyJobView.as_view()),
    path("applications/list/", ApplicationListView.as_view()),
    path("applications/<int:id>/", ApplicationStatusUpdateView.as_view()),
]
