from django.db import models

class APIRequestLog(models.Model):
    ip_address = models.GenericIPAddressField()
    user = models.CharField(max_length=255, null=True, blank=True)
    endpoint = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ip_address} - {self.endpoint} - {'Blocked' if self.is_blocked else 'Allowed'}"
