from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unit_number = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=15, default='N/A') 

    def __str__(self):
        return self.user.username
    
class MaintenanceRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    block_number = models.CharField(max_length=100)
    room_number = models.CharField(max_length=100)
    unit_type = models.CharField(max_length=100)
    issue_description = models.TextField()
    attachment = models.ImageField(upload_to='attachments/', null=True, blank=True)
    unit_number = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='Pending')  # Add status field
    created_at = models.DateTimeField(auto_now_add=True)  # Add created_at field

    def __str__(self):
        return f"{self.unit_type} request from {self.user.username} - {self.status}"
