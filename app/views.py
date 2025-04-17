from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ConsultationRequest

# Create your views here.

#global variables 
def global_vars(request):
    og_site_name = f'{request.user.username} from Vortfolio shares' if request.user.is_authenticated else 'Vortfolio'

    return {
        'siteName': 'Vortfolio',
        'author':'Abdullah',
        'og_site_name':og_site_name,
        'logo':'https://lh3.googleusercontent.com/pw/AP1GczOGutgra7QDYHKh6So_zvBBe7oZ17qLabQT68A4JGpN06fQ__3F47qiBBh_RmU0EhmAOdp-K9j9li5ARd97yh1UvICqt45ATlYcuoskceWPfymdTyq28YN9eK7958crO3UfRDHQE7GktH1d0r0VPzs=w575-h429-s-no-gm?authuser=0',
        'views':'Subscribers',
    }
def index(request):
    
    context = {
        'title': 'Vortfolio ',
        'description':'Vortfolio delivers expert web development, AI solutions, and student-focused tech education in one powerful platform.',
        'keywords':'Vortfolio, Web Development, AI Solutions, Digital Portfolio, Professional Portfolio, Vortfolio Platform, Full Stack Development',
        'og_title':'Vortfolio - Professional Web Development, AI & Digital Solutions Platform',
        'og_description':'Vortfolio delivers cutting-edge web development, AI integration, and digital solutions. Transform your digital presence with Vortfolio\'s innovative platform.',
        'og_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'og_image_alt':'Vortfolio',
        'og_type': 'website',
        'og_url': 'Vortfolio',

        #twitter card
        
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Vortfolio - Professional Web Development, AI & Digital Solutions Platform',
        'twitter_description': 'Vortfolio - Your gateway to professional web development and AI solutions. Experience innovation with Vortfolio\'s comprehensive digital services.',
        'twitter_image': 'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'twitter_image_alt': 'Vortfolio',
        'twitter_url': 'Vortfolio',
        # 'twitter_card_type': 'summary_large_image',
        
        'twitter_title': 'Vortfolio | Professional Web Development & Digital Solutions',

    }
    return render(request, "index.html" ,context)
def about(request):
    context = {
        'title': 'About - Vortfolio AI Based Software Development',
        'description':'Vortfolio – A premier platform delivering expert web development, cutting-edge AI solutions, and innovative digital services. We also offer tailored learning resources and services for students, empowering the next generation of tech professionals. Discover next-generation technology and educational support with Vortfolio.',
        'keywords':'Vortfolio, Web Development, AI Solutions, Digital Portfolio, Professional Portfolio, Vortfolio Platform, Full Stack Development',
        'og_title':'Vortfolio - Professional Web Development, AI & Digital Solutions Platform',
        'og_description':'Vortfolio delivers cutting-edge web development, AI integration, and digital solutions. Transform your digital presence with Vortfolio\'s innovative platform.',
        'og_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'og_image_alt':'Vortfolio',
        'og_type': 'website',
        'og_url': request.build_absolute_uri(),

        #twitter card
        
        'twitter_card': 'summary_large_image',
        'twitter_title': 'About Vortfolio - Professional Web Development, AI & Digital Solutions Platform',
        'twitter_description': 'Vortfolio - Your gateway to professional web development and AI solutions. Experience innovation with Vortfolio\'s comprehensive digital services.',
        'twitter_image': 'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'twitter_image_alt': 'Vortfolio',
        'twitter_url': request.build_absolute_uri(),
        # 'twitter_card_type': 'summary_large_image',
        
        'twitter_title': 'Vortfolio | Professional Web Development & Digital Solutions',

    }
    return render(request, "about.html" , context)
def projects(request):
    context = {
        'title': 'Vortfolio - Professional Web Development, AI & Digital Solutions Platform',
        'description':'Vortfolio – A premier platform delivering expert web development, cutting-edge AI solutions, and innovative digital services. We also offer tailored learning resources and services for students, empowering the next generation of tech professionals. Discover next-generation technology and educational support with Vortfolio.',
        'keywords':'Vortfolio, Web Development, AI Solutions, Digital Portfolio, Professional Portfolio, Vortfolio Platform, Full Stack Development',
        'og_title':'Vortfolio - Professional Web Development, AI & Digital Solutions Platform',
        'og_description':'Vortfolio delivers cutting-edge web development, AI integration, and digital solutions. Transform your digital presence with Vortfolio\'s innovative platform.',
        'og_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'og_image_alt':'Vortfolio',
        'og_type': 'website',
        'og_url': request.build_absolute_uri(),

        #twitter card
        
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Vortfolio - Professional Web Development, AI & Digital Solutions Platform',
        'twitter_description': 'Vortfolio - Your gateway to professional web development and AI solutions. Experience innovation with Vortfolio\'s comprehensive digital services.',
        'twitter_image': 'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'twitter_image_alt': 'Vortfolio',
        'twitter_url': request.build_absolute_uri(),
        # 'twitter_card_type': 'summary_large_image',
        
        'twitter_title': 'Vortfolio | Professional Web Development & Digital Solutions',

    }
    return render(request, "projects.html",)
def services(request):
    context = {
        'title': 'Vortfolio - Professional Web Development, AI & Digital Solutions Platform',
        'description':'Vortfolio – A premier platform delivering expert web development, cutting-edge AI solutions, and innovative digital services. We also offer tailored learning resources and services for students, empowering the next generation of tech professionals. Discover next-generation technology and educational support with Vortfolio.',
        'keywords':'Vortfolio, Web Development, AI Solutions, Digital Portfolio, Professional Portfolio, Vortfolio Platform, Full Stack Development',
        'og_title':'Vortfolio - Professional Web Development, AI & Digital Solutions Platform',
        'og_description':'Vortfolio delivers cutting-edge web development, AI integration, and digital solutions. Transform your digital presence with Vortfolio\'s innovative platform.',
        'og_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'og_image_alt':'Vortfolio',
        'og_type': 'website',
        'og_url': request.build_absolute_uri(),

        #twitter card
        
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Vortfolio - Professional Web Development, AI & Digital Solutions Platform',
        'twitter_description': 'Vortfolio - Your gateway to professional web development and AI solutions. Experience innovation with Vortfolio\'s comprehensive digital services.',
        'twitter_image': 'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'twitter_image_alt': 'Vortfolio',
        'twitter_url': request.build_absolute_uri(),
        # 'twitter_card_type': 'summary_large_image',
        
        'twitter_title': 'Vortfolio | Professional Web Development & Digital Solutions',

    }
    return render(request, "services.html" , context)
@csrf_exempt
def contact(request):
    context = {
        'title': 'Vortfolio - Professional Web Development, AI & Digital Solutions Platform',
        'description':'Vortfolio – A premier platform delivering expert web development, cutting-edge AI solutions, and innovative digital services. We also offer tailored learning resources and services for students, empowering the next generation of tech professionals. Discover next-generation technology and educational support with Vortfolio.',
        'keywords':'Vortfolio, Web Development, AI Solutions, Digital Portfolio, Professional Portfolio, Vortfolio Platform, Full Stack Development',
        'og_title':'Vortfolio - Professional Web Development, AI & Digital Solutions Platform',
        'og_description':'Vortfolio delivers cutting-edge web development, AI integration, and digital solutions. Transform your digital presence with Vortfolio\'s innovative platform.',
        'og_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'og_image_alt':'Vortfolio',
        'og_type': 'website',
        'og_url': request.build_absolute_uri(),

        #twitter card
        
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Vortfolio - Professional Web Development, AI & Digital Solutions Platform',
        'twitter_description': 'Vortfolio - Your gateway to professional web development and AI solutions. Experience innovation with Vortfolio\'s comprehensive digital services.',
        'twitter_image': 'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'twitter_image_alt': 'Vortfolio',
        'twitter_url': request.build_absolute_uri(),
        # 'twitter_card_type': 'summary_large_image',
        
        'twitter_title': 'Vortfolio | Professional Web Development & Digital Solutions',

    }
    if request.method == 'GET':
        return render(request, 'contact.html' , context)
    
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
    context = {
        'title': 'Vortfolio - Professional Web Development, AI & Digital Solutions Platform',
        'description':'Vortfolio – A premier platform delivering expert web development, cutting-edge AI solutions, and innovative digital services. We also offer tailored learning resources and services for students, empowering the next generation of tech professionals. Discover next-generation technology and educational support with Vortfolio.',
        'keywords':'Vortfolio, Web Development, AI Solutions, Digital Portfolio, Professional Portfolio, Vortfolio Platform, Full Stack Development',
        'og_title':'Vortfolio - Professional Web Development, AI & Digital Solutions Platform',
        'og_description':'Vortfolio delivers cutting-edge web development, AI integration, and digital solutions. Transform your digital presence with Vortfolio\'s innovative platform.',
        'og_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'og_image_alt':'Vortfolio',
        'og_type': 'website',
        'og_url': request.build_absolute_uri(),

        #twitter card
        
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Vortfolio - Professional Web Development, AI & Digital Solutions Platform',
        'twitter_description': 'Vortfolio - Your gateway to professional web development and AI solutions. Experience innovation with Vortfolio\'s comprehensive digital services.',
        'twitter_image': 'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'twitter_image_alt': 'Vortfolio',
        'twitter_url': request.build_absolute_uri(),
        # 'twitter_card_type': 'summary_large_image',
        
        'twitter_title': 'Vortfolio | Professional Web Development & Digital Solutions',

    }
    return render(request, "portfolio.html" , context)

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
def learn(request):
    context ={
        'description':'A comprehensive web development roadmap from beginner to professional level. Learn HTML, CSS, JavaScript, Django, and more.',
        'keywords':'Vortfolio, Web Development, AI Solutions, Digital Portfolio, Professional Portfolio, Vortfolio Platform, Full Stack Development, Learn Web Development, Learn AI, Learn Digital Solutions',
    }
    # Fix the template path by using forward slashes and removing the backslash
    return render(request, "Services/learn.html" )


def ads_txt(request):
    content = "google.com, pub-1234567890123456, DIRECT, f08c47fec0942fa0"
    return HttpResponse(content, content_type='text/plain')

def robots_txt(request):
    content = (
        "User-agent: *\n"
        "Disallow: /admin/\n"
        "Allow: /\n"
        "Sitemap: https://www.vortfolio.icu/sitemap.xml\n"  # Replace with your actual domain
    )
    return HttpResponse(content, content_type="text/plain")

def consultation_detail(request, id):
    consultation = get_object_or_404(ConsultationRequest, id=id)
    return render(request, 'consultation_detail.html', {'consultation': consultation})


def learning_sd(request):
    return render(request, 'Services/learn_Software_development.html')

def roadmap(request):
    return render(request, 'Services/roadmap.html')