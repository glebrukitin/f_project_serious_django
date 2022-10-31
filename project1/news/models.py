from django.db import models

class New(models.Model):
    image = models.ImageField(upload_to='news/')
    title = models.CharField(max_length=200)
    text_1 = models.TextField()
    quote = models.CharField(max_length=200)
    text_2 = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/news/{self.id}/'