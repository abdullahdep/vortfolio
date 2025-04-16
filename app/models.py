# Create your models here.
from django.db import models
from django.urls import reverse

class ConsultationRequest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    company_website = models.URLField(blank=True, null=True)
    industry = models.CharField(max_length=100)
    company_size = models.CharField(max_length=50)
    goals = models.TextField()
    need_website = models.BooleanField(default=False)
    need_app = models.BooleanField(default=False)
    need_learning = models.BooleanField(default=False)
    agreed_terms = models.BooleanField(default=False)
    get_updates = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.company_email}"

    def get_absolute_url(self):
        # Replace 'consultation_detail' with the name of the URL pattern for viewing a single ConsultationRequest
        return reverse('consultation_detail', args=[self.id])