from django.db import models

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=200)
    # featured_img = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    body = models.TextField()

    def __str__(self):
        return self.title
