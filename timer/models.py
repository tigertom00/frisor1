from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Timer(models.Model):
    """Model definition for Timeliste."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    dato = models.DateField(null=True, blank=True)
    text = models.CharField(max_length=64, blank=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Timer."""

        verbose_name = 'time'
        verbose_name_plural = 'timer'

    def __str__(self):
        """Unicode representation of Timer."""
        return self.user.username
