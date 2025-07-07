#!/bin/bash
echo "🚀 Запуск бота через Webhook..."

if [ -z "$TOKEN" ]; then
  echo "❌ Variable TOKEN не установлена!"
  exit 1
fi

if ! command -v python3 &> /dev/null; then
  echo "❌ Python3 не найден!"
  exit 1
fi

if [ ! -f "bible_bot_webhook.py" ]; then
  echo "❌ bible_bot_webhook.py не найден!"
  exit 1
fi

python3 bible_bot_webhook.py
