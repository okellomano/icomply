from django import forms
from .models import PoliciesDocuments

from multiupload.fields import MultiFileField


class UploadForm(forms.Form):
    policies = MultiFileField(min_num=1, max_num=8, max_file_size=1024*1024*5)


class PoliciesUploadForm(forms.ModelForm):
    class Meta:
        model = PoliciesDocuments
        fields = ('privacy', 'data_protection', 'data_retention', 'data_security', 'system_use_procedures', 'data_sharing_agreements', 'data_processor_contracts')

