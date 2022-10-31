from django.db import models
from django.conf import settings

from news.models import New
from places.models import Place


class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(New, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.firstname} comment {self.text[0:20]} {self.date_created}'
    
    class Meta:
        unique_together = ['user', 'text', 'post']



class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.firstname} comment {self.text[0:20]} {self.date_created}'

    class Meta:
        unique_together = ['user', 'text', 'place']


