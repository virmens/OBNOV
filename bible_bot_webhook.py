import os
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    ContextTypes
)
from telegram.constants import ParseMode
from aiohttp import web

TOKEN = os.environ.get("TOKEN")
PORT = int(os.environ.get("PORT", 5000))


BIBLE_BOOKS = [
    "Бытие", "Исход", "Левит", "Числа", "Второзаконие",
    "Иисус Навин", "Судей", "Руфь", "1 Царств", "2 Царств",
    "3 Царств", "4 Царств", "1 Паралипоменон", "2 Паралипоменон", "Ездра",
    "Неемия", "Есфирь", "Иов", "Псалтирь", "Притчи", "Екклесиаст", "Песнь Песней",
    "Исаия", "Иеремия", "Плач Иеремии", "Иезекииль", "Даниил",
    "Осия", "Иоиль", "Амос", "Авдий", "Иона", "Михей", "Наум", "Аввакум",
    "Софония", "Аггей", "Захария", "Малахия",

    "Матфея", "Марка", "Луки", "Иоанна", "Деяния","Иакова", "1 Петра", "2 Петра",
    "1 Иоанна", "2 Иоанна", "3 Иоанна", "Иуды"
    "Римлянам", "1 Коринфянам", "2 Коринфянам",
    "Галатам", "Ефесянам", "Филиппийцам", "Колосянам",
    "1 Фессалоникийцам", "2 Фессалоникийцам",
    "1 Тимофею", "2 Тимофею", "Титу", "Филимону",
    "Евреям", "Откровение"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keboard = [[InlineKeyboardButton("🎡 Крутить колесо", callback_data='spin')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("👋 Привет! Нажми, чтобы выбрать книгу:", reply_markup=reply_markup)

async def spin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    book = random.choice(BIBLE_BOOKS)
    keyboard = [[InlineKeyboardButton("🎡 Ещё раз", callback_data='spin')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.reply_text(f"📖 Тебе выпала книга: *{book}*", parse_mode=ParseMode.MARKDOWN, reply_markup=reply_markup)

async def main():
    assert TOKEN, "Не задана TOKEN!"
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(spin))

    # Webhook-endpoint
    async def handler(request):
        data = await request.json()
        update = Update.de_json(data, app.bot)
        await app.process_update(update)
        return web.Response()

    aio_app = web.Application()
    aio_app.router.add_post(f"/{TOKEN}", handler)

    # Регистрация webhook у Telegram
    url = f"https://{HOST}/{TOKEN}"
    await app.bot.set_webhook(url)
    print(f"✅ Webhook установлен: {url}")

    web.run_app(aio_app, host="0.0.0.0", port=PORT)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())