from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

class Sessions(models.Model):
    trip_number = models.URLField(
        _("Trip Number"), 
        max_length=128, 
        db_index=True, 
        unique=True, 
        blank=True
    )
# # main title
# # short paragraph
# # link to binder
