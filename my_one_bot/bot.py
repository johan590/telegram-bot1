import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Включим логирование, чтобы видеть ошибки
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Токен, который вы получили от BotFather
TOKEN = "8054977543:AAHlY0lFzdOpK9UrOkgCvbnb3IWm9d99FOE"

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_html(
        f"Привет, {user.mention_html()}! Я эхо-бот. Напиши что-нибудь, и я повторю."
    )

# Обработчик команды /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Я просто повторю всё, что ты скажешь.")

# Обработчик обычных текстовых сообщений
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Повторяем текст пользователя
    await update.message.reply_text(update.message.text)

def main():
    # Создаем Application
    application = Application.builder().token(TOKEN).build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Регистрируем обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Запускаем бота на опрос серверов Telegram
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()