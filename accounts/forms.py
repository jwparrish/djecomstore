from django import forms
from djecomstore.accounts.models import UserProfile

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ('user',)