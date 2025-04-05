from django.db import models

class Consultation(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    company_name = models.CharField(max_length=200, blank=True, null=True)  # Optional
    company_website = models.URLField(blank=True, null=True)  # Optional
    industry = models.CharField(max_length=100, blank=False, null=False)
    company_size = models.CharField(max_length=50, blank=False, null=False)
    challenges = models.TextField(blank=False, null=False)
    needs_website = models.BooleanField(default=False, )
    needs_app = models.BooleanField(default=False,)
    for_learning = models.BooleanField(default=False,)
    agreed_to_terms = models.BooleanField(default=False, blank=False, null=False)
    wants_updates = models.BooleanField(default=False, )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.created_at}"
