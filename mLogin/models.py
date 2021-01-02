from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	muser = models.OneToOneField(User, on_delete=models.CASCADE)
	Phonenumber = models.CharField(verbose_name="phone number",max_length=10)