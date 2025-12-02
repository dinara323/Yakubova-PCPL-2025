import datetime
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import requests

# ===================== КОНФИГУРАЦИЯ =====================
# Способ 1: Через config.py (создайте файл config.py с токенами)
try:
    from config import TELEGRAM_TOKEN, OPENWEATHER_TOKEN
except ImportError:
    # Способ 2: Через переменные (замените на свои токены)
    TELEGRAM_TOKEN = "ВАШ_TELEGRAM_TOKEN_ЗДЕСЬ"
    OPENWEATHER_TOKEN = "ВАШ_OPENWEATHER_TOKEN_ЗДЕСЬ"

# ===================== НАСТРОЙКА ЛОГИРОВАНИЯ =====================
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ===================== СЛОВАРЬ СМАЙЛИКОВ =====================
code_to_smile = {
    "Clear": "Ясно ☀️",
    "Clouds": "Облачно ☁️",
    "Rain": "Дождь 🌧",
    "Drizzle": "Морось 🌦",
    "Thunderstorm": "Гроза ⛈",
    "Snow": "Снег ❄️",
    "Mist": "Туман 🌫",
    "Smoke": "Дым 💨",
    "Haze": "Мгла 😶‍🌫️",
    "Dust": "Пыль 💨",
    "Fog": "Туман 🌁",
    "Sand": "Песчаная буря 🌪",
    "Ash": "Пепел 🌋",
    "Squall": "Шквал 💨",
    "Tornado": "Торнадо 🌪"
}

# ===================== КОМАНДА /start =====================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_text = (
        f"Привет, {user.first_name}! 👋\n\n"
        "Я бот погоды 🌤️\n\n"
        "Просто отправь мне название города, и я покажу текущую погоду.\n"
        "Например: Москва, London, Paris\n\n"
        "Доступные команды:\n"
        "/start - начать диалог\n"
        "/help - помощь\n"
        "/weather [город] - узнать погоду\n"
        "/about - о боте"
    )
    await update.message.reply_text(welcome_text)

# ===================== КОМАНДА /help =====================
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "📋 Как пользоваться ботом:\n\n"
        "1. Просто отправьте название города текстом:\n"
        "   Например: Москва\n\n"
        "2. Или используйте команду:\n"
        "   /weather Москва\n\n"
        "3. Поддерживаются города на русском и английском:\n"
        "   Санкт-Петербург, New York, Berlin\n\n"
        "Доступные команды:\n"
        "/start - начать\n"
        "/help - эта справка\n"
        "/about - информация о боте"
    )
    await update.message.reply_text(help_text)

# ===================== КОМАНДА /about =====================
async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = (
        "🌤️ Weather Bot v1.0\n\n"
        "Бот показывает текущую погоду в любом городе мира.\n"
        "Использует данные OpenWeatherMap API.\n\n"
        "Разработчик: Ваше имя\n"
        "Источник данных: openweathermap.org"
    )
    await update.message.reply_text(about_text)

# ===================== КОМАНДА /weather =====================
async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "Пожалуйста, укажите город.\n"
            "Пример: /weather Москва\n"
            "Или просто отправьте название города текстом."
        )
        return
    
    city = ' '.join(context.args)
    await get_weather(update, city)

# ===================== ОБРАБОТКА ТЕКСТА =====================
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    city = update.message.text.strip()
    await get_weather(update, city)

# ===================== ФУНКЦИЯ ПОЛУЧЕНИЯ ПОГОДЫ =====================
async def get_weather(update: Update, city: str):
    try:
        # Показываем статус "печатает..."
        await update.message.chat.send_action(action="typing")
        
        # Формируем URL запроса
        url = f"http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': OPENWEATHER_TOKEN,
            'units': 'metric',
            'lang': 'ru'
        }
        
        # Отправляем запрос
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        
        # Проверяем ответ
        if data.get('cod') != 200:
            error_msg = data.get('message', 'Неизвестная ошибка')
            await update.message.reply_text(f"❌ Ошибка: {error_msg}")
            return
        
        # Извлекаем данные
        city_name = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        weather_desc = data['weather'][0]['main']
        description = data['weather'][0]['description']
        
        # Получаем смайлик
        weather_emoji = code_to_smile.get(weather_desc, "🌈")
        
        # Время восхода и заката
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M')
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M')
        
        # Формируем ответ
        weather_info = (
            f"📍 *{city_name}, {country}*\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"🌡 Температура: *{temp:.1f}°C*\n"
            f"🤔 Ощущается как: *{feels_like:.1f}°C*\n"
            f"📊 Давление: *{pressure} hPa*\n"
            f"💧 Влажность: *{humidity}%*\n"
            f"💨 Ветер: *{wind_speed} м/с*\n"
            f"☁️ Погода: {weather_emoji} {description.capitalize()}\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"🌅 Восход: {sunrise}\n"
            f"🌇 Закат: {sunset}\n\n"
            f"Хорошего дня! ✨"
        )
        
        await update.message.reply_text(weather_info, parse_mode='Markdown')
        
    except requests.exceptions.Timeout:
        await update.message.reply_text("⏰ Превышено время ожидания ответа от сервера погоды.")
    except requests.exceptions.ConnectionError:
        await update.message.reply_text("🔌 Ошибка подключения к интернету.")
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        await update.message.reply_text("❌ Произошла ошибка. Попробуйте позже.")

# ===================== ОБРАБОТКА ОШИБОК =====================
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Ошибка: {context.error}")
    try:
        await update.message.reply_text("⚠️ Произошла ошибка. Попробуйте снова.")
    except:
        pass

# ===================== ОСНОВНАЯ ФУНКЦИЯ =====================
def main():
    # Проверяем токены
    if TELEGRAM_TOKEN == "ВАШ_TELEGRAM_TOKEN_ЗДЕСЬ":
        print("❌ ОШИБКА: Укажите Telegram токен!")
        print("1. Создайте файл config.py с содержанием:")
        print("   TELEGRAM_TOKEN = 'ваш_токен'")
        print("   OPENWEATHER_TOKEN = 'ваш_токен'")
        print("\n2. Или замените токены прямо в этом файле")
        print("\n3. Получите токены:")
        print("   - Telegram: @BotFather")
        print("   - OpenWeather: openweathermap.org")
        return
    
    if OPENWEATHER_TOKEN == "ВАШ_OPENWEATHER_TOKEN_ЗДЕСЬ":
        print("❌ ОШИБКА: Укажите OpenWeather токен!")
        return
    
    # Создаем приложение
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("weather", weather_command))
    application.add_handler(CommandHandler("about", about_command))
    
    # Обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    
    # Обработчик ошибок
    application.add_error_handler(error_handler)
    
    # Запускаем бота
    print("=" * 50)
    print("✅ Бот запускается...")
    print("📱 Проверьте бота в Telegram")
    print("🛑 Для остановки нажмите Ctrl+C")
    print("=" * 50)
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)

# ===================== ЗАПУСК =====================
if __name__ == '__main__':
    main()