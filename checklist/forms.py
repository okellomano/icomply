from django import forms
from .models import Checklist, DpaChecklist, ChecklistsModel

from django.contrib.auth import get_user_model


class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        # fields = ('protection', 'encrypt', 'policy')
        fields = ('protection',)


class DpaChecklistForm(forms.ModelForm):
    class Meta:
        model = DpaChecklist
        fields = ('organization', 'governance', 'privacy', 'security')


# form for adding a checklist
class AddChecklistForm(forms.ModelForm):
    class Meta:
        model = ChecklistsModel
        fields = '__all__'

