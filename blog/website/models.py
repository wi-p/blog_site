from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
   

class Publication(models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField(null = True)
    date = models.DateField()
    view_number = models.IntegerField(default = 0)
    writter = models.ForeignKey(User, on_delete = models.CASCADE)
    photo = models.FileField(upload_to = 'images/website/pubs', null = True)
    slug = models.SlugField(unique = True, blank = True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Publication, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    
    