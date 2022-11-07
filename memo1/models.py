from importlib.resources import contents
from unicodedata import category
from django.db import models
# Create your models here.



class study_web(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    category = models.TextField(null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    url = models.URLField(null=True,blank=True)
#重要度を示すもの
    def __str__(self):
        return str(self.content)



