from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='user_profile_pics/',  default='default-avatar.png', null=True, blank=True)

    def __str__(self):
        return f"{self.user} Profile"

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()
