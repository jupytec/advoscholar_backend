"""Contact Us Model"""
from core.models import BaseModel
from django.db import models


class ContactUs(BaseModel):
    """Contact Us Model"""
    email = models.EmailField(db_index=True)
    full_name = models.CharField(max_length=255)
    message = models.TextField()
    enquiry_type = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    objects = models.Manager() # The default manager.

    def __str__(self):
        return str(self.email)
