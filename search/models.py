from django.db import models

# Create your models here.
class SearchDB(models.Model):
    unique_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=355)
    slug = models.CharField(max_length=234)

    def __str__(self):
        return 'Search Content: ' + 'Slug: ' + self.slug 
    