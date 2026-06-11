import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser






# Create your models here.
class RoleChoicess(models.TextChoices):
    ADMIN = 'ADMIN', 'ADMIN'
    CANDIDATE = 'CANDIDATE', 'CANDIDATE'
    VIEWER = 'VIEWER', 'VIEWER'


class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=RoleChoicess.choices, default=RoleChoicess.VIEWER)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


## create the models
class UserProfile(models.Model):
    primary_key = models.AutoField(primary_key=True)
    unique_id = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    class Meta:
        db_table = 'User_profile'
        ordering = ['-primary_key']
        verbose_name = "USER PROFILE"
        verbose_name_plural = "USER PROFILES"

    
    def __str__(self):
        return f" {self.user.username} - {self.user.role}"



