from django import forms
from account.models import User
class UserForm (forms.ModelForm):
    class Meta:
        # specify model to be used
        model = User
        fields = '__all__'