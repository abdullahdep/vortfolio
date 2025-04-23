from django.contrib import admin
from .models import ConsultationRequest

@admin.register(ConsultationRequest)
class ConsultationRequestAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company_email', 'phone_number', 'industry', 'created_at')
    list_filter = ('industry', 'company_size', 'need_website', 'need_app', 'need_learning')
    search_fields = ('first_name', 'last_name', 'company_email', 'company_name')
    readonly_fields = ('created_at', 'updated_at')
# Register your models here.


