from telegram.ext import Updater, CommandHandler
import requests

BOT_TOKEN = "**************************************************"   # no spaces
WEATHER_API_KEY = "****************************************"


def start(update, context):
    update.message.reply_text(
        "Hello 👋\nUse:\n/weather <city>\nExample: /weather Delhi"
    )
    
def weather(update, context):
    if len(context.args) == 0:
        update.message.reply_text("Please provide a city name.\nExample: /weather Mumbai")
        return
    
    city = " ".join(context.args)
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={WEATHER_API_KEY}&units=metric"
    )
    
    response = requests.get(url).json()
    
    if response.get("cod") != 200:
        update.message.reply_text("❌ City not found")
        return
    
    temp = response["main"]["temp"]
    feels = response["main"]["feels_like"]
    desc = response["weather"][0]["description"]
    
    reply = (
        f"🌍 City: {city}\n"
        f"🌡 Temperature: {temp}°C\n"
        f"🤒 Feels like: {feels}°C\n"
        f"☁️ Condition: {desc}"
    )
        
    update.message.reply_text(reply)
    
updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("weather", weather))

print("🤖 Bot is running...")
updater.start_polling()
updater.idle()
