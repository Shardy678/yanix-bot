# 🎵 yanix-bot

Простой Discord-бот, который:

* подключается к голосовому каналу
* принимает ссылку (YouTube и др.)
* извлекает аудио
* воспроизводит его в голосовом канале 

---

## 🚀 Возможности

* `!join` — подключиться к голосовому каналу
* `!leave` — выйти из голосового канала
* `!play <url>` — воспроизвести аудио по ссылке
* `!hello` — тестовая команда

---

## 📦 Требования

### 1️⃣ Python

* Python **3.11+**

### 2️⃣ FFmpeg

Бот **не будет работать без FFmpeg**.

#### Linux (Ubuntu/Debian)

```bash
sudo apt install ffmpeg
```

#### Windows

Скачать с [https://ffmpeg.org/](https://ffmpeg.org/) и добавить в `PATH`

Проверка:

```bash
ffmpeg -version
```

---

### 3️⃣ Node.js (ОБЯЗАТЕЛЬНО)

YouTube теперь требует JS-рантайм для извлечения потоков.

#### Установка

```bash
node --version
```

Если команды нет:

* Linux: `sudo apt install nodejs npm`
* Windows: [https://nodejs.org/](https://nodejs.org/)

---

## 📥 Установка

```bash
git clone <repo-url>
cd yanix-bot

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\\Scripts\\activate     # Windows

pip install -r requirements.txt
```

### `requirements.txt`

```txt
discord.py
yt-dlp
python-dotenv
```

---

## 🔐 Переменные окружения

Создай файл `.env` в корне проекта:

```env
DISCORD_TOKEN=your_bot_token_here
```

Токен берётся в Discord Developer Portal.

---

## ▶️ Запуск

```bash
python discord_bot.py
```

Если всё ок, бот появится онлайн.

---
