from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

class Usr(UserCreationForm):
	class Meta:
		model = User
		fields = ["username"]

