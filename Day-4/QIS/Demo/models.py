from django.db import models

# Create your models here.
class UsrReg(models.Model):
	user_name = models.CharField(max_length=120)
	pass_word = models.CharField(max_length=100)
	email = models.EmailField(max_length=120)
	age = models.IntegerField(default=18)   