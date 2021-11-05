from  django.db.models.signals import post_save  #this signal gets fired after object is saved
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save , sender = User)
def create_profile(sender , instance , created , **kwargs):
    if created:
        Profile.objects.create(user = instance)

# create_profile creates the profile for the current user , when the signal(post_save) is received 


#now saving the the profile

@receiver(post_save , sender = User)
def save_profile(sender , instance , **kwargs):
    instance.profile.save()

#after this jusgt go in apps.py file and create ready method and import this signals file there.