from django import forms
from .models import Checklist, DpaChecklist


class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        # fields = ('protection', 'encrypt', 'policy')
        fields = ('protection',)


class DpaChecklistForm(forms.ModelForm):
    class Meta:
        model = DpaChecklist
        fields = ('organization', 'governance', 'privacy', 'security')

