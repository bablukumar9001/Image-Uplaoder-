from django.db import models

# Create your models here.


class Image(models.Model):

    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)
    caption = models.CharField(max_length=300 ,default=' image caption')


def __str__(self):
    return self.caption
