from django.db import models

# Create your models here.
class Meeting(models.Model):
  STARTED = "Started"
  COMPLETED = "Completed"
  STATUS = [
    (STARTED, "started"),
    (COMPLETED, "Completed")
  ]

  title = models.CharField(max_length=200, null=False, blank=False)
  description = models.TextField(null=True, blank=False)
  status = models.CharField(max_length=200, choices=STATUS,default=STARTED)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
def __str__(self):
    return self.title