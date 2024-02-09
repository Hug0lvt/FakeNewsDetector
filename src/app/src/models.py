from django.db import models

# Create your models here.

class Text(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    
    class Meta:
        app_label = 'app'
    
    def __str__(self):
        return self.title

