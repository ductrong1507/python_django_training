from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField()
    last_name = models.EmailField()
    email_name = models.CharField()
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
