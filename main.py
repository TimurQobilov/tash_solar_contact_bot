from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = ""

# Кнопки
main_keyboard = ReplyKeyboardMarkup(
    [["Цены", "Контакты"]],
    resize_keyboard=True
)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Выберите нужный пункт ниже:",
        reply_markup=main_keyboard
    )

# Обработка кнопок
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Цены":
        await update.message.reply_text("🔧 Услуги и цены:"
                                        "\n— 1 кВт — 4 млн сум (он-грид), 5 млн сум с аккумулятором (гибрид)"
                                        "\n— 2 кВт — 8 млн сум (он-грид), 10 млн сум с аккумулятором (гибрид)"
                                        "\n— 3 кВт — 12 млн сум (он-грид), 15 млн сум с аккумулятором (гибрид)"
                                        "\n— 5 кВт — 20 млн сум (он-грид), 25 млн сум с аккумулятором (гибрид)"
                                        "\n— 6 кВт — 24 млн сум (он-грид), 30 млн сум с аккумулятором (гибрид)"
                                        "\n— 7 кВт — 28 млн сум (он-грид), 35 млн сум с аккумулятором (гибрид)"
                                        "\n— 10 кВт — 40 млн сум (он-грид), 50 млн сум с аккумулятором (гибрид)"
                                        "\n— 15, 20, 30, 50 кВт — по договорённости")
    elif text == "Контакты":
        await update.message.reply_text("📞 Контакты:"
                                        "\n+998970051465"
                                        "\n+998884705040"
                                        "\n+998886696868"
                                        "\n+998994970207")
    else:
        await update.message.reply_text("Пожалуйста, выбери один из пунктов ниже 👇", reply_markup=main_keyboard)

# Запуск бота
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен 🚀")
    app.run_polling()

if __name__ == "__main__":
    main()
