from django.db import models

BOOL_CHOICES = ((True, 'Publicado'), (False, 'Nao publicado'))

class Category(models.Model):
    title = models.CharField(max_length=200)
    alias = models.CharField(max_length=250, blank=True, null=True)
    published = models.BooleanField(choices=BOOL_CHOICES)

    def __unicode__(self):
        return self.title

class Post(models.Model):
    category = models.ForeignKey(Category)
    
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    text = models.TextField(max_length=600) 
    published = models.BooleanField(choices=BOOL_CHOICES)
    keywords = models.CharField(blank=True, null=True, max_length=250)

    def __unicode__(self):
        return self.title
