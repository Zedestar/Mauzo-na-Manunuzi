from django.contrib.auth.models import User 
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Description of your management command'

    def handle(self, *args, **options):
        # Your code for cleaning up the database goes here
        # Example: Get valid user IDs, exclude invalid ones, and delete them
        valid_user_ids = User.objects.values_list('id', flat=True)
        invalid_user_ids = User.objects.exclude(id__in=valid_user_ids)
        invalid_user_ids.delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleaned up the database'))
