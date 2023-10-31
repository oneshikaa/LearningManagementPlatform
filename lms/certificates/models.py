from django.db import models
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Certificate(models.Model):
    # student = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    certificate_file = models.FileField(upload_to='certificates/')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # Define the URL to view the certificate details if needed
        return reverse('certificate_detail', kwargs={'pk': self.pk})

