import sys
import os

# Add project root to the path so this file can be run as a standalone file
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'remind_me.settings')
import django
django.setup()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram_bot.models import TelegramUser
from decouple import config
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User

# sync_to_async utility of django to safely run the sync django code in async context
@sync_to_async
def save_telegram_user(chat_id, username, user):
    TelegramUser.objects.get_or_create(
        chat_id=chat_id,
        defaults={'username': username, 'user': user}
    )

@sync_to_async
def save_django_user(username):
    user, _ = User.objects.get_or_create(username=username)
    return user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.username
    print(username)
    chat_id = update.effective_user.id
    
    user = await save_django_user(username)
    print(user)

    await save_telegram_user(chat_id, username, user)
    await update.message.reply_text("👋 Welcome! You'll receive reminders here.")

def main():
    token = config('TELEGRAM_BOT_TOKEN')
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()

    

