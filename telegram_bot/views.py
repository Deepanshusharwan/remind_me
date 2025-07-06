from rest_framework.permissions import IsAuthenticated
from rest_framework.response  import Response
from rest_framework.views import APIView
from telegram_bot.serializer import ReminderSerializer
from telegram_bot.models import Reminder, TelegramUser


class ReminderCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            try:
                telegram_user = TelegramUser.objects.get(user=request.user)
                reminder = serializer.save(user=telegram_user)
                return Response(ReminderSerializer(reminder).data, status=201)
            except TelegramUser.DoesNotExist:
                return Response({"error": "No Telegram account linked."}, status=400)
        return Response(serializer.errors, status=400)
