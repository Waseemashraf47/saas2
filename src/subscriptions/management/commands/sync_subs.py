from django.core.management.base import BaseCommand

from subscriptions.models import Subscription

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        # print("Bismillah")
        qs = Subscription.objects.filter(active=True)
        for obj in qs:
            # print(obj.groups.all())
            sub_perms = obj.permission.all()
            for group in obj.groups.all():
                group.permissions.set(sub_perms)
                # for per in obj.permission.all():
                #     group.permissions.add(per)
            # print(obj.permission.all())