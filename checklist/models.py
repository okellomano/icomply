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
    protection = models.BooleanField('Take Data Protection into account at all times', default=False)
    encrypt = models.BooleanField('Encrypt, pseudonymize, or anonymize personal data whenever possible', default=False)
    policy = models.BooleanField('Create an internal security policy for your team members, and build awareness about data protection', default=False)


class DpaChecklist(models.Model):
    organization = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    governance = MultiSelectField(choices=GOVERNANCE)
    privacy = MultiSelectField(choices=PRIVACY_RIGHTS)
    security = MultiSelectField(choices=DATA_SECURITY)



