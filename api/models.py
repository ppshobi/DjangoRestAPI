from django.db import models

# Create your models here.

class BucketList(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)
