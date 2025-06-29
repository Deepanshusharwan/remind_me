from django.db import models

class TelegramUser(models.Model):
    username = models.CharField(max_length=100, blank=True)
    chat_id = models.BigIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username or str(self.chat_id)


class Reminder(models.Model):
    user = models.ForeignKey("TelegramUser", on_delete=models.CASCADE)
    message = models.TextField()
    remind_at = models.DateTimeField()
    sent = models.BooleanField(default=False)

    def __str__(self):
        return f"Reminder [{self.message[:20]} @ {self.remind_at}]"
