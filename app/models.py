from django.db import models
from django.contrib.auth.models import AbstractUser

class StudentResponse(models.Model):
    response = models.TextField()
    expert_responses = models.ManyToManyField('ExpertResponse', blank=True)

    def __str__(self):
        return  self.response[:50] 

class ExpertResponse(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    sentence = models.TextField(default='')
    knowledge = models.TextField(default='')
    confidence = models.TextField(default='')
    strength = models.TextField(default='')
    comments = models.TextField(default='')

    def __str__(self):
        return f"{self.user.username}: {self.sentence[:20]}"

class User(AbstractUser):
    current_response = models.ForeignKey('StudentResponse', on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.current_response:
            # Get the first entry in the StudentResponse model
            default_response = StudentResponse.objects.first()
            self.current_response = default_response
        super().save(*args, **kwargs)