from django.db import models
from django.contrib.auth import get_user_model

from multiselectfield import MultiSelectField


GOVERNANCE = (
    ('g1', 'Appoint a Data Protection Officer (if necessary)'),
    ('g2', 'Designate someone responsible for ensuring DPA compliance in your organization'),
    ('g3', 'Sign a data processing agreement between your organization and third parties')
)

PRIVACY_RIGHTS = (
    ('pr1', 'It is easy for your customers to ask you to stop processing their data'),
    ('pr2', 'It is easy for your customers to request you t have their personal data deleted'),
    ('pr3', 'It is easy for your customers to correct or update inaccurate of incomplete information'),
    ('pr4', 'It is easy for your customers to request and receive all the information you have about them')
)

DATA_SECURITY = (
    ('ds1', 'Have internal security policy for your team members, and build awareness on data protection'),
    ('ds2', 'Have a mechanism to notify authorities and data subjects in the event of a data breach'),
    ('ds3', 'Encrypt or anonymize personal data wherever possible')
)


class Checklist(models.Model):
    # organization = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    protection = models.CharField(max_length=100)
    # encrypt = models.BooleanField('Encrypt, or anonymize personal data whenever possible', default=False)
    # policy = models.BooleanField('Create an internal security policy for your team members', default=False)


class DpaChecklist(models.Model):
    organization = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    governance = MultiSelectField(choices=GOVERNANCE)
    privacy = MultiSelectField(choices=PRIVACY_RIGHTS)
    security = MultiSelectField(choices=DATA_SECURITY)


class Governance(models.Model):
    dpo = models.BooleanField('Appoint a Data Protection Officer (if necessary)', default=False)
    dpa_implementation = models.BooleanField('Designate someone responsible for ensuring DPA compliance in your organization', default=False)
    agreement = models.BooleanField('Sign a data processing agreement between your organization and third parties', default=False)


class PrivacyRights(models.Model):
    stop_processing = models.BooleanField('It is easy for your customers to ask you to stop processing their data', default=False)
    delete_data = models.BooleanField('It is easy for your customers to request you t have their personal data deleted', default=False)
    update = models.BooleanField('It is easy for your customers to correct or update inaccurate of incomplete information', default=False)
    request_info = models.BooleanField('It is easy for your customers to request and receive all the information you have about them', default=False)


class DataSecurity(models.Model):
    policies = models.BooleanField('Have internal security policy for your team members, and build awareness on data protection', default=False)
    notification = models.BooleanField('Have a mechanism to notify authorities and data subjects in the event of a data breach', default=False)
    encryption = models.BooleanField('Encrypt or anonymize personal data wherever possible', default=False)


class UsersChecklist(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    data_security = models.ManyToManyField(DataSecurity)
    privacy = models.ManyToManyField(PrivacyRights)
    governance = models.ManyToManyField(Governance)


class ChecklistsModel(models.Model):
    description = models.CharField(max_length=100)
    checklist_item1 = models.CharField(max_length=250)
    checklist_item2 = models.CharField(max_length=250)
    checklist_item3 = models.CharField(max_length=250)
    checklist_item4 = models.CharField(max_length=250)
    checklist_item5 = models.CharField(max_length=250)
    score = models.CharField(max_length=250)

    def __str__(self):
        return self.description
