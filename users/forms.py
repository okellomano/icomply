from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms
from allauth.account.forms import SignupForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')


# Custom sign up form extending django_allauth
class CustomSignupForm(SignupForm):
    name = forms.CharField(max_length=100, label='Organization/Company Name')
    address = forms.CharField(max_length=100, label='Location')

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'name', 'address')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.name = self.cleaned_data['name']
        user.address = self.cleaned_data['address']
        user.save()
        return user
