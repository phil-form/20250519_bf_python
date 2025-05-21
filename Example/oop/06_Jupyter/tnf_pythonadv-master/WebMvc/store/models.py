from django.db import models

class Composer(models.Model):
    lastname = models.CharField(max_length=40, null=False)
    firstname = models.CharField(max_length=40, null=False)
    
    def __str__(self) -> str:
        return self.lastname + " " + self.firstname
    
class Compilation(models.Model):
    title = models.CharField(max_length=50)
    artists = models.ManyToManyField(Composer, related_name='album', blank=True)