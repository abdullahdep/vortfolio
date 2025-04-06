from django.shortcuts import render
from django.http import JsonResponse
from .models import Consultation
from django.db.models import Q
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
            
            # Check if user already exists with same email or phone
            existing_user = Consultation.objects.filter(
                Q(email=data['companyEmail']) | Q(phone_number=data['phoneNumber'])
            ).first()
            
            if existing_user:
                # If this is a new submission request
                if data.get('submitNew'):
                    # Create new record
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
                        needs_website=data.get('source1', False),
                        needs_app=data.get('source2', False),
                        for_learning=data.get('source3', False),
                        agreed_to_terms=data['source4'],
                        wants_updates=data.get('source5', False)
                    )
                    return JsonResponse({'status': 'success'})
                # If this is an update confirmation
                elif data.get('confirmUpdate'):
                    # Update existing record
                    existing_user.first_name = data['firstName']
                    existing_user.last_name = data['lastName']
                    existing_user.email = data['companyEmail']
                    existing_user.phone_number = data['phoneNumber']
                    existing_user.company_name = data.get('companyName', '')
                    existing_user.company_website = data.get('companyWebsite', '')
                    existing_user.industry = data['industry']
                    existing_user.company_size = data['companySize']
                    existing_user.challenges = data['goals']
                    existing_user.needs_website = data.get('source1', False)
                    existing_user.needs_app = data.get('source2', False)
                    existing_user.for_learning = data.get('source3', False)
                    existing_user.agreed_to_terms = data['source4']
                    existing_user.wants_updates = data.get('source5', False)
                    existing_user.save()
                    
                    return JsonResponse({
                        'status': 'success',
                        'message': 'Your information has been updated successfully!'
                    })
                else:
                    # Return existing user data for confirmation
                    return JsonResponse({
                        'status': 'exists',
                        'message': 'User already exists',
                        'existingData': {
                            'firstName': existing_user.first_name,
                            'lastName': existing_user.last_name,
                            'companyEmail': existing_user.email,
                            'phoneNumber': existing_user.phone_number,
                            'companyName': existing_user.company_name,
                            'companyWebsite': existing_user.company_website,
                            'industry': existing_user.industry,
                            'companySize': existing_user.company_size,
                            'goals': existing_user.challenges,
                            'source1': existing_user.needs_website,
                            'source2': existing_user.needs_app,
                            'source3': existing_user.for_learning,
                            'source4': existing_user.agreed_to_terms,
                            'source5': existing_user.wants_updates
                        }
                    }, status=200)
            
            # If no existing user, proceed with regular validation and creation
            required_fields = [
                'firstName', 'lastName', 'companyEmail', 'phoneNumber',
                'industry', 'companySize', 'goals', 'source4'
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
                needs_website=data.get('source1', False),
                needs_app=data.get('source2', False),
                for_learning=data.get('source3', False),
                agreed_to_terms=data['source4'],
                wants_updates=data.get('source5', False)
            )
            return JsonResponse({'status': 'success'})
            
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
    return render(request, "contact.html", siteName)
def portfolio(request):
    return render(request, "portfolio.html", siteName)
