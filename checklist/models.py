from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.urls import reverse

# from reports.base import ModelReport


def validate_file_extension(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError(u'Please upload PDF documents only.')


class Category(models.Model):
    type = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.type


class Checklist(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    checklist_item = models.CharField(max_length=300)
    brief_description = models.TextField(max_length=300, default='Required for DPA compliance')
    value = models.IntegerField()
    implemented = models.BooleanField('Implemented', default=False)

    def __str__(self):
        return self.checklist_item

    @property
    def percentage_score(self):
        pass


# class UserChecklist(models.Model):
#     user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
#     user_checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE, related_name='user_checklist')
#     user_score = models.ForeignKey(Checklist, on_delete=models.CASCADE, related_name='user_score')
#     date_filled = models.DateTimeField(auto_now_add=True)
#     percentage_score = models.IntegerField(default=0)
#
#     class Meta:
#         verbose_name_plural = 'User Checklists'


class PoliciesDocuments(models.Model):
    ''''''
    organization = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    policy_name = models.CharField(max_length=50)
    privacy = models.FileField(upload_to='policies/', null=True, blank=True, validators=[validate_file_extension])
    data_protection = models.FileField(upload_to='policies/', null=True, blank=True, validators=[validate_file_extension])
    data_retention = models.FileField(upload_to='policies/', null=True, blank=True, validators=[validate_file_extension])
    data_security = models.FileField(upload_to='policies/', null=True, blank=True, validators=[validate_file_extension])
    system_use_procedures = models.FileField(upload_to='policies/', null=True, blank=True, validators=[validate_file_extension])
    data_sharing_agreements = models.FileField(upload_to='policies/', null=True, blank=True, validators=[validate_file_extension])
    data_processor_contracts = models.FileField(upload_to='policies/', null=True, blank=True, validators=[validate_file_extension])

    class Meta:
        verbose_name_plural = 'Policies Documents'


class UserChecklistEntries(models.Model):
    '''User results model. '''
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE, null=True, blank=True)
    percent_s = models.PositiveIntegerField(default=0)
    total_values = models.PositiveIntegerField(default=0)
    user_score = models.PositiveIntegerField(default=0)
    tier = models.CharField(max_length=20, default='Non-compliant')
    date_filled = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'User Checklist Entries'

    def __str__(self):
        return f'{self.user} {self.percent_s} {self.tier} {self.user_score} {self.total_values}'


# class ChecklistReport(ModelReport):
#     ame = "Report"
#     queryset = UserChecklistEntries.objects.all()
#
#     def get_field_lookups(self):
#         fields = [self.queryset.user, self.queryset.percent_s, self.queryset.user_score,
#                   self.queryset.tier, self.queryset.total_values
#                   ]
#         return fields
