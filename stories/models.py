from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='stories/')
    answer = models.TextField()
    resolution_image = models.ImageField(upload_to='stories/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'

    def __str__(self):
        return self.title