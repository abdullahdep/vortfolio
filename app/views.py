from django.shortcuts import render
from django.http import JsonResponse
from .models import Consultation
import json

# Create your views here.

siteName = "Vortfolio"

siteName= {"siteName": siteName}


def index(request):
    return render(request, "index.html" ,siteName)
def about(request):
    return render(request, "about.html" ,  siteName)
def projects(request):
    return render(request, "projects.html", siteName)
def services(request):
    return render(request, "services.html", siteName)
def contact(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Validate required fields (removing the optional fields)
            required_fields = [
                'firstName', 'lastName', 'companyEmail', 'phoneNumber',
                'industry', 'companySize', 'goals', 'source4'  # Only keep required fields
            ]
            
            for field in required_fields:
                if field not in data or not data[field]:
                    return JsonResponse({
                        'status': 'error',
                        'message': f'Field {field} is required'
                    }, status=400)
            
            consultation = Consultation.objects.create(
                first_name=data['firstName'],
                last_name=data['lastName'],
                email=data['companyEmail'],
                phone_number=data['phoneNumber'],
                company_name=data.get('companyName', ''),
                company_website=data.get('companyWebsite', ''),
                industry=data['industry'],
                company_size=data['companySize'],
                challenges=data['goals'],
                needs_website=data.get('source1', False),  # Made optional
                needs_app=data.get('source2', False),      # Made optional
                for_learning=data.get('source3', False),   # Made optional
                agreed_to_terms=data['source4'],           # Required
                wants_updates=data.get('source5', False)   # Made optional
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
    return render(request, "contact.html", siteName)
def portfolio(request):
    return render(request, "portfolio.html", siteName)
