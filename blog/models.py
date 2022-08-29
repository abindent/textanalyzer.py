from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.timezone import now


from search.models import SearchDB

from cloudinary.models import CloudinaryField

# Create your models here.
class Blog(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    user=models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    author=models.CharField(default="Unkown Author", max_length=60)
    slug=models.CharField(max_length=130)
    views= models.IntegerField(default=0)
    publish = models.BooleanField(default=False, null=True)
    gist = models.CharField(default=None, max_length=300)
    timeStamp=models.DateTimeField(blank=True, null=True, auto_now=True)
    thumbnail = CloudinaryField(null=True, blank=True, folder="TextAnalyser/blog/images")
    comments = models.IntegerField(null=True, blank=True, default=0)
    content=models.TextField()


    def __str__(self):
        return self.title + " by " + self.author

class Comment(models.Model):
    sno= models.AutoField(primary_key=True)
    comments=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.comments[0:13] + "..." + "by" + " " + self.user.username

@receiver(post_save, sender=Blog)
def _post_save_receiver(sender, instance: Blog, created, **kwargs):
    if created:
        SearchDB.objects.create(title=instance.title, description=instance.gist[:335], slug=f"blog/{instance.slug}")

@receiver(post_delete, sender=Blog)
def _post_delete_receiver(sender, instance: Blog, **kwargs):
    
    obj = SearchDB.objects.filter(slug=f"blog/{instance.slug}")

    if not obj.exists():
       _obj_title = SearchDB.objects.filter(title__icontains=f"{instance.title}")
       _obj_description = SearchDB.objects.filter(description__icontains=f"{instance.gist[:335]}")
       obj = SearchDB.objects.filter(slug__icontains=f"blog/{instance.slug}").union(_obj_title, _obj_description).first()
       
    obj.delete()