from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # extend later if you need phone, loyalty tier, etc.
    pass


class CustomerProfile(models.Model):
    user          = models.OneToOneField(User, on_delete=models.CASCADE)
    joined_at     = models.DateTimeField(auto_now_add=True)
    last_seen     = models.DateTimeField(null=True, blank=True)
    churn_score   = models.FloatField(default=0.0)   # 0 … 1
    # cached fields you’ll compute nightly
    spend_90d     = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.user.get_full_name() or self.user.username
