from django.db import models


# class Appl(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField(default=1)
#
#
# class AcademicInstitution(models.Model):
#     institution = models.CharField(max_length=100)
#     date_from = models.DateField()
#     date_to = models.DateField()
#     achievements = models.FileField(upload_to='media/%Y/%m/%d')
#     appl = models.ForeignKey(Appl, on_delete=models.CASCADE, null=True)


# class Checklist(models.Model):
#     description = models.CharField(max_length=200)
#     checked = models.BooleanField(default=False)
#
#
# class Organization(models.Model):
#     org_name = models.CharField(max_length=50)
#     email = models.EmailField()
#     address = models.CharField(max_length=100)
#     bs_licence_no = models.CharField(max_length=10)
#
#
# class Category(models.Model):
#     description = models.CharField(max_length=10)
#     organization = models.ForeignKey(Organization)
#
#
# class Report(models.Model):
#     pass
#
#
# class Compliance(models.Model):
#     pass
#
