from django.db import models
from django.db.models import permalink

# Create your models here.

class Bolgpost(models.Model):
    title=models.CharField(max_length=100,unique=True)
    author=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    body=models.TextField()
    posted=models.DateField(db_index=True,auto_now_add=True)

    def __unicode__(self):
        return '%s'%self.title

    # 返回博客链接
    @permalink
    def get_absolute_url(self):
        return ('view_bolg_post',None,{'slug':self.slug})

