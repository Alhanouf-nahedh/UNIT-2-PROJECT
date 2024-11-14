from django.db import models

# Model for storing contact messages
class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)