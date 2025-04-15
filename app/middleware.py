import time
import logging
from django.http import Http404

logger = logging.getLogger(__name__)

class AdsTxtMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/ads.txt':
            start_time = time.time()
            response = self.get_response(request)
            duration = time.time() - start_time
            
            logger.info(
                f"ads.txt request from {request.META.get('REMOTE_ADDR')} "
                f"completed in {duration:.2f}s with status {response.status_code}"
            )
            
            if response.status_code == 404:
                logger.error("ads.txt file not found")
                raise Http404("ads.txt not found")
                
            return response
        return self.get_response(request)