from django.contrib.auth.models import AbstractUser
from django.db import models

from shop.models import compress_image


class User(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_image', null=True, blank=True)
    phone_number = models.CharField(max_length=16)

    def save(self, *args, **kwargs):
        try:
            self.profile_image = compress_image(self.profile_image, new_width=370)
            super().save(*args, **kwargs)
        except:
            super().save(*args, **kwargs)
