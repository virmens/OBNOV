from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import random

import os

TOKEN = os.getenv("TOKEN")


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
    keyboard = [[InlineKeyboardButton("🎡 Крутить колесо", callback_data='spin')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
    "👋 Привет! Нажми на кнопку, чтобы случайным образом выбрать книгу из Библии:",
    reply_markup=reply_markup,
    parse_mode='Markdown'
)


async def spin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    book = random.choice(BIBLE_BOOKS)
    keyboard = [[InlineKeyboardButton("🎡 Крутить ещё раз", callback_data='spin')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.message.reply_text(
        text=f"📖 Тебе выпала книга: *{book}*",
        parse_mode='Markdown',
        reply_markup=reply_markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Вот доступные команды:\n"
        "/start - начать работу с ботом\n"
        "/help - получить эту помощь"
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(spin))
    print("✅ Бот запущен. Открой Telegram и отправь /start")
    app.run_polling()

if __name__ == '__main__':
    main()
