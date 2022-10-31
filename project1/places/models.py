from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    is_pamyatnik = models.BooleanField(default=False)
    image_1 = models.ImageField(upload_to='place/')
    image_2 = models.ImageField(upload_to='place/')
    image_3 = models.ImageField(upload_to='place/')
    text_1 = models.TextField()
    text_2 = models.TextField()
    text_3 = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.is_pamyatnik:
            return f'/places/{self.id}/'
        if not self.is_pamyatnik:
            return f'/places/{self.id}/'