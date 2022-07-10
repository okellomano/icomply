from django.db import models
from django.contrib.auth import get_user_model


class Checklist(models.Model):
    # organization = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    protection = models.BooleanField('Take Data Protection into account at all times', default=False)
    encrypt = models.BooleanField('Encrypt, pseudonymize, or anonymize personal data whenever possible', default=False)
    policy = models.BooleanField('Create an internal security policy for your team members, and build awareness about data protection', default=False)



