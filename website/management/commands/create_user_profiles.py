from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from website.models import UserProfile

class Command(BaseCommand):
    help = 'Creates user profiles for users that do not have one'

    def handle(self, *args, **kwargs):
        users_without_profile = User.objects.filter(profile__isnull=True)
        count = 0
        for user in users_without_profile:
            UserProfile.objects.get_or_create(user=user)
            count += 1
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {count} user profiles'
            )
        )
