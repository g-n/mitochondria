from django.db import models
from profiles.models import profiles

from django.utils.translation import ugettext_lazy as _

from common.models import Address, User


class Profiles(models.Model):
    first_name = models.CharField(_("First name"), max_length=255)
    last_name = models.CharField(_("Last name"), max_length=255)


    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['-created_on']
