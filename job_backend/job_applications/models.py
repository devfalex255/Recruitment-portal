import uuid
from django.db import models
from job_auth.models import User



# Create your models here.
class ApplicationStatus(models.TextChoices):
    PENDIG = 'PENDING', 'PENDING'
    ACCEPTED = 'ACCEPTED', 'ACCEPTED'
    REJECTED = 'REJECTED', 'REJECTED'


class Job(models.Model):
    primary_key = models.AutoField(primary_key=True)
    unique_id = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=200)
    description = models.TextField()
    posted_by = models.ForeignKey(User, related_name="posted_by", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


    class Meta:
        db_table = 'jobs'
        ordering = ['-primary_key']
        verbose_name = 'JOB APPLICATION'
        verbose_name_plural = 'JOB APPLICATIONS'

    
    def __str__(self):
        return self.title




class Application(models.Model):
    primary_key = models.AutoField(primary_key=True)
    unique_id = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    job = models.ForeignKey(Job, related_name="jobs_applicants", on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, related_name="applicant", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=ApplicationStatus.choices, default=ApplicationStatus.PENDIG)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


    class Meta:
        db_table = 'job_applications'
        ordering = ['-primary_key']
        verbose_name = 'JOBS APPLICATION'
        verbose_name_plural = 'JOBS APPLICATIONS'
        unique_together = ("job", "applicant")

    
    def __str__(self):
        return f"{self.applicant.username} -> {self.job.title}"


