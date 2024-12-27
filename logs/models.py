import datetime
from django.db import models
from django.utils import timezone

class Log(models.Model):
    log_text = models.CharField(max_length=5000)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.log_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)