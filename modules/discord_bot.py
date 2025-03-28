r"""
    ## Модуль для роботи з Discord ботом
    ### Тут ми налаштовуємо, як наш бот (WorldIT_Helper) буде спілкуватися з сервером Discord.
"""
import discord, dotenv, os

# Завантажуємо змінні середовища з файлу .env там зберігаються  токен бота щоб не вкрали 
dotenv.load_dotenv()
# Беремо токен бота з середовища з файлу .env
# Токен - це як пароль для бота, щоб Discord знав що це наш бот та ні в якому разні не показувати токен иншим 
TOKEN = os.getenv('TOKEN')

# Кажемо Discord що нас цікавить у повідомленнях наприклад, текст повідомлень
intents = discord.Intents.default()
intents.message_content = True

# Створюємо "бота" - об'єкт, який буде представляти нашого бота в Discord
bot = discord.Client(intents=intents)

# Це подія происходит коли бот успішно підключився до Discord
@bot.event
async def on_ready():
    print("Бот запущенно") 


@bot.event
# Це теж  подія яка происходит  коли з'являється повідомлення в чаті
async def on_message(message):
    # Перевіряємо, чи автор повідомлення - не сам бот (щоб не було спама від бота )
    if message.author != bot.user:
        # Беремо текст повідомлення
        content = message.content
        # Перевіряємо, чи є текст в повідомленні 
        if content:
            # Відправляємо назад в канал те саме повідомлення, що і отримали (Бот просто повторює все, що йому пишуть)
            await message.channel.send(content)