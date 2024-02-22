from django.contrib.auth.models import User
from django.db import models

# Get the first user in the database
def get_default_user_id():
    default_user = User.objects.first()
    if default_user:
        return default_user.id
    else:
        return None  # If there are no users in the database

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user_id)
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False) 

    def __str__(self):
        return self.taskTitle
