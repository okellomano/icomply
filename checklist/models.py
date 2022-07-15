from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Category(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Checklist(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    checklist_item = models.CharField(max_length=150)
    value = models.IntegerField()
    implemented = models.BooleanField('Implemented', default=False)

    def __str__(self):
        return self.checklist_item

    # on submit, redirect to the results page
    def get_absolute_url(self):
        return reverse('checklist:results')


class UserChecklist(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    user_checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE, related_name='user_checklist')
    user_score = models.ForeignKey(Checklist, on_delete=models.CASCADE, related_name='user_score')
    date_filled = models.DateTimeField(auto_now_add=True)

