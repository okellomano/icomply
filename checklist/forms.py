from django import forms
from .models import Checklist


class PoliciesUploadForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    name = forms.CharField(max_length=50)


# class UserChecklistForm(forms.ModelForm):
#     class Meta:
#         model = Checklist
#         fields = ['category', 'checklist_item', 'implemented']


