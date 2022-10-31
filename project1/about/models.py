from django.db import models

class About(models.Model):
    about_image = models.ImageField(upload_to='about/')
    text_about = models.TextField()
    title_about = models.TextField()
    text_1 = models.TextField()
    text_2 = models.TextField()
    text_3 = models.TextField()
    image_1 = models.ImageField(upload_to='about/')
    image_2 = models.ImageField(upload_to='about/')
    image_3 = models.ImageField(upload_to='about/')
    image_4 = models.ImageField(upload_to='about/')
    image_5 = models.ImageField(upload_to='about/')
    image_6 = models.ImageField(upload_to='about/')
    image_7 = models.ImageField(upload_to='about/')
    image_8 = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.title_about

    def get_image_urls(self):
        images = [self.image_1,self.image_2,self.image_3,self.image_4,self.image_5,self.image_6,self.image_7,self.image_8]
        urls = [image.url for image in images]
        return urls

class GaleryPhoto(models.Model):
    image = models.ImageField(upload_to='galery/')
