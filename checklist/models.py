from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


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


class UserChecklist(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    user_checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE, related_name='user_checklist')
    user_score = models.ForeignKey(Checklist, on_delete=models.CASCADE, related_name='user_score')
    date_filled = models.DateTimeField(auto_now_add=True)
    percentage_score = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'User Checklists'


class PoliciesDocuments(models.Model):
    organization = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    policy_name = models.CharField(max_length=50)
    document = models.FileField(upload_to='policies/')

    class Meta:
        verbose_name_plural = 'Policies Documents'


class UserChecklistEntries(models.Model):
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
        return f'{self.user}'.title()

