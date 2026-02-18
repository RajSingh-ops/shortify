from django.db import models
class Url(models.Model):
    id=models.AutoField(primary_key=True)
    url1=models.URLField()