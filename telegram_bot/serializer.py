from rest_framework import serializers
from telegram_bot.models import Reminder

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ['id', 'message', 'remind_at']
