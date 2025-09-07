from django.core.management.base import BaseCommand
from wpfront.models import Page

class Command(BaseCommand):
    help = 'Creates initial page data'

    def handle(self, *args, **kwargs):
        # Create a home page
        Page.objects.get_or_create(
            slug='home',
            defaults={
                'title': 'Home Page',
                'content': '<h1>Welcome to the Home Page</h1><p>This is the default content.</p>'
            }
        )
        self.stdout.write(self.style.SUCCESS('Successfully created initial page data'))
