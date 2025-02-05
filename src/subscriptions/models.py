from django.db import models
from django.contrib.auth.models import Group, Permission
# Create your models here.

SUBSCRIPTION_PERMISSIONS = [
            ("advanced", "Advanced Perm"), # subscription.advance
            ("pro", "Pro Perm"), # subscription.pro
            ("basic", "Basic Perm"), # subscription.basic
            ("basic_ai", "Basic AI Perm"), # subscription.basic
        ]

class Subscription(models.Model):
    name = models.CharField(max_length=120)
    active = models.BooleanField(default=True)
    groups = models.ManyToManyField(Group)
    permission = models.ManyToManyField(Permission, limit_choices_to={"content_type__app_label": "subscriptions",
    # "codename__in": ["basic", "basic_ai", "advanced", "pro"]
    "codename__in": [x[0]for x in SUBSCRIPTION_PERMISSIONS]
    }
                                        )
    
    class Meta:
        permissions = SUBSCRIPTION_PERMISSIONS