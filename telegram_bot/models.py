from django.db import models

class TelegramUser(models.Model):
    username = models.CharField(max_length=100, blank=True)
    chat_id = models.BigIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username or str(self.chat_id)
