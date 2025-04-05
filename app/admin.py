from django.contrib import admin
from .models import Consultation

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'company_name', 'created_at')
    list_filter = ('industry', 'company_size', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'company_name')
    date_hierarchy = 'created_at'
# Register your models here.







