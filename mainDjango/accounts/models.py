from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import logging
logr = logging.getLogger(__name__)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    shortbio = models.TextField(max_length=100,blank=True,null=True)
    fblink = models.URLField(blank=True,null=True)
    twlink = models.URLField(blank=True,null=True)
    gplink = models.URLField(blank=True,null=True)
    dob = models.DateField(blank=True,null=True)

    
    
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


@receiver(post_save, sender=User)
def make_sure_user_profile_is_added_on_user_created(sender, **kwargs):
    if kwargs.get('created', False):
        up = UserProfile.objects.create(user=kwargs.get('instance'))
        logr.debug("UserProfile created: %s" % up)