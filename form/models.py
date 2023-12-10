from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    published = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')
