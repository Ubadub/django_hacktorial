from django.db import models

# Create your models here.

class Post(models.Model):
    # TODO: Define fields here

    title = models.CharField(unique=True, max_length=50)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

    # @models.permalink
    # def get_absolute_url(self):
    #     return ('')

    # TODO: Define custom methods here

    