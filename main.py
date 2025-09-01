import requests
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "7922175837:AAEJl1ht9fJwPwPLE6BFx8xNnGFGyjYmiZw"

# === Клавиатура ===
main_keyboard = ReplyKeyboardMarkup(
    [["Погода", "Цены", "Контакты"]],
    resize_keyboard=True
)

# === Получение погоды ===
def get_weather(location: str = 'Ташкент') -> str:
    url = f"https://wttr.in/{location}?format=j1&lang=ru"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        current = data['current_condition'][0]
        temperature = current['temp_C']
        wind_speed = current['windspeedKmph']
        humidity = current['humidity']
        pressure = current['pressure']
        visibility = current['visibility']
        description = current['lang_ru'][0]['value']

        return (f"☁️ Погода в {location.title()}:\n"
                f"🌡️ Температура: {temperature}°C\n"
                f"📝 Описание: {description}\n"
                f"💨 Ветер: {wind_speed} км/ч\n"
                f"💧 Влажность: {humidity}%\n"
                f"📈 Давление: {pressure} мбар\n"
                f"👁️ Видимость: {visibility} км")
    except:
        return "⚠️ Ошибка: не удалось получить данные о погоде."

# === /start ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Выберите пункт в меню ниже или напишите название города:",
        reply_markup=main_keyboard
    )

# === Обработка кнопок и текста ===
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text == "Цены":
        await update.message.reply_text(
            "🔧 Услуги и цены:"
            "\n— 1 кВт — 4 млн сум (он-грид), 5 млн сум с аккумулятором (гибрид)"
            "\n— 2 кВт — 8 млн сум (он-грид), 10 млн сум с аккумулятором (гибрид)"
            "\n— 3 кВт — 12 млн сум (он-грид), 15 млн сум с аккумулятором (гибрид)"
            "\n— 5 кВт — 20 млн сум (он-грид), 25 млн сум с аккумулятором (гибрид)"
            "\n— 6 кВт — 24 млн сум (он-грид), 30 млн сум с аккумулятором (гибрид)"
            "\n— 7 кВт — 28 млн сум (он-грид), 35 млн сум с аккумулятором (гибрид)"
            "\n— 10 кВт — 40 млн сум (он-грид), 50 млн сум с аккумулятором (гибрид)"
            "\n— 15, 20, 30, 50 кВт — по договорённости"
        )

    elif text == "Контакты":
        await update.message.reply_text(
            "📞 Контакты:"
            "\n+998970051465"
            "\n+998884705040"
            "\n+998886696868"
            "\n+998994970207"
        )

    elif text == "Погода":
        await update.message.reply_text("🌍 Напиши название города, чтобы узнать погоду:")

    else:
        # Пытаемся интерпретировать как город
        weather_info = get_weather(text)
        await update.message.reply_text(weather_info)

# === Запуск ===
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🚀 Бот запущен")
    app.run_polling()

if __name__ == "__main__":
    main()