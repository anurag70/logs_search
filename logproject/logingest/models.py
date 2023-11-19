from django.db import models


class Log(models.Model):
    level = models.CharField(max_length=255)
    message = models.TextField(null=True, default=None)
    traceId = models.CharField(max_length=255)
    spanId = models.CharField(max_length=255)
    commit = models.CharField(max_length=255)    
    resourceId = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    metadata = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.timestamp} - {self.level} - {self.message}"

