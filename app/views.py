from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ConsultationRequest

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
@csrf_exempt
def contact(request):
    if request.method == 'GET':
        return render(request, 'contact.html')
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Check if user already exists
            existing_request = ConsultationRequest.objects.filter(company_email=data['companyEmail']).first()
            
            if existing_request and not data.get('confirmUpdate') and not data.get('submitNew'):
                return JsonResponse({
                    'status': 'exists',
                    'existingData': {
                        'firstName': existing_request.first_name,
                        'lastName': existing_request.last_name,
                        'companyEmail': existing_request.company_email,
                        'phoneNumber': existing_request.phone_number
                    }
                })
            
            if existing_request and data.get('confirmUpdate'):
                # Update existing record
                existing_request.first_name = data['firstName']
                existing_request.last_name = data['lastName']
                existing_request.phone_number = data['phoneNumber']
                existing_request.company_name = data['companyName']
                existing_request.company_website = data['companyWebsite']
                existing_request.industry = data['industry']
                existing_request.company_size = data['companySize']
                existing_request.goals = data['goals']
                existing_request.need_website = data['source1']
                existing_request.need_app = data['source2']
                existing_request.need_learning = data['source3']
                existing_request.agreed_terms = data['source4']
                existing_request.get_updates = data['source5']
                existing_request.save()
            else:
                # Create new record
                ConsultationRequest.objects.create(
                    first_name=data['firstName'],
                    last_name=data['lastName'],
                    company_email=data['companyEmail'],
                    phone_number=data['phoneNumber'],
                    company_name=data['companyName'],
                    company_website=data['companyWebsite'],
                    industry=data['industry'],
                    company_size=data['companySize'],
                    goals=data['goals'],
                    need_website=data['source1'],
                    need_app=data['source2'],
                    need_learning=data['source3'],
                    agreed_terms=data['source4'],
                    get_updates=data['source5']
                )
            
            return JsonResponse({'status': 'success'})
            
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def portfolio(request):
    return render(request, "portfolio.html", siteName)
