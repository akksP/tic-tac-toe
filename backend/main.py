from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackContext

# Ваш токен бота
TOKEN = "7319162102:AAEpW1IpILjukNF0fmQOHSXl7HsfR9DmItI"

# Обработчик команды /start
async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Mini-App", web_app=WebAppInfo(url="https://example.com"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Добро пожаловать!",
        reply_markup=reply_markup
    )

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    # Регистрация команды /start
    application.add_handler(CommandHandler("start", start))

    # Запуск бота
    application.run_polling()

if __name__ == "__main__":
    main()
