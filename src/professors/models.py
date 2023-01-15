from django.db import models
from django.utils import timezone

class Professor(models.Model):
    name = models.CharField(max_length=255)
    personal_information = models.TextField()
    education = models.TextField()
    work_and_related_experience = models.TextField()
    awards_and_honors = models.TextField()
    activities_hobbies = models.TextField()
    skills = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='professor', default='professor/default.jpg', blank=True, null=True)


    def __str__(self):
        return self.name
    
