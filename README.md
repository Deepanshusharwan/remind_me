# 🛎️ Remind Me

**Remind Me** is a Django-based task reminder service that integrates with a Telegram bot. Users can create reminders via a REST API and receive notification messages through Telegram. The system uses Celery with Redis for scheduling and background task processing.

---

## 📦 Features

- ✅ User authentication via Django
- 🔒 Token-based API access
- 🤖 Telegram bot integration
- ⏰ Reminder creation with date/time
- 🔔 Notifications delivered via Telegram
- 📬 Telegram users auto-linked with Django users
- 🧵 Background task queue using **Celery + Redis**

---

## 🚀 Technologies

- Django & Django REST Framework
- Telegram Bot API
- Celery with Redis
- SQLite (default DB)
- Python 3.13+
- curl/Postman support

---

## 📁 Project Structure

├─ .env
├─ .git
├─ .gitignore
├─ .python-version
├─ .venv
├─ README.md
├─ Readme.md
├─ api
│ ├─ **init**.py
│ ├─ admin.py
│ ├─ apps.py
│ ├─ migrations
│ │ ├─ **init**.py
│ ├─ models.py
│ ├─ serializers.py
│ ├─ tasks.py
│ ├─ tests.py
│ ├─ urls.py
│ └─ views.py
├─ db.sqlite3
├─ manage.py
├─ pyproject.toml
├─ remind_me
│ ├─ **init**.py
│ ├─ asgi.py
│ ├─ celery.py
│ ├─ settings.py
│ ├─ urls.py
│ └─ wsgi.py
├─ requirements.txt
├─ telegram_bot
│ ├─ **init**.py
│ ├─ admin.py
│ ├─ apps.py
│ ├─ bot.py
│ ├─ migrations
│ │ ├─ 0001_initial.py
│ │ ├─ **init**.py
│ ├─ models.py
│ ├─ serializer.py
│ ├─ tests.py
│ └─ views.py
└─ uv.lock
Total directories: 10
Total files: 63

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/remind_me.git
cd remind_me
```

### 2. Create a virtual enviroment

```
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Enviroment configuration

```
TELEGRAM_BOT_TOKEN=your_telegram_token_here
SECRET_KEY=your_django_secret_key
DEBUG=True

```

### 5. Migrare and create superuser

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

```

### 6. Start redis (in a docker container)

```
docker run -d -p 6379:6379 -p 8001:8001 --name redis redis
```

### 7. Start service

**start Django server**

```
python manage.py runserver
```

**Start Celery worker**

```
celery -A remind_me worker -l info
```

**Running the telegram bot**

```
python telegram_bot/bot.py
```

## API Usage

### 1. Get Auth Token

```
curl -X POST http://127.0.0.1:8000/api/token/ -d "username=YOUR_USERNAME&password=YOUR_PASSWORD"

```

### 2. Create a reminder

```
curl -X POST http://127.0.0.1:8000/api/reminders/create \
-H "Authorization: Token YOUR_TOKEN" \
-H "Content-Type: application/json" \
-d '{"remind_at": "2025-06-30T10:30:00Z", "message": "Water the plants"}'

```

## TODO

- Frontend interface (maybe React)

* Recurring reminders
* Timezone support
* Voice command via telegram

## Licence

MIT Licence. Use freely for personal or educational projects just give credits.♥

## Author

Made with ♥ by [Deepanshu Sharwan](https://github.com/deepanshusharwan) | Gmail: deepanshusharwan35@gmail.com
