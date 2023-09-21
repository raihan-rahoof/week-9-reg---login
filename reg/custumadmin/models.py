from django.db import models

# Create your models here.
class users(models.Model):
    first_name=models.CharField(max_length=50,verbose_name="First name")
    last_name=models.CharField(max_length=50,verbose_name="Last name")
    username=models.CharField( max_length=50 , verbose_name="Username")
    email=models.EmailField(max_length=254,verbose_name="Email")

    def __str__(self):
        return str(self.username)