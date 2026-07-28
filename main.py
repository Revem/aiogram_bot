import asyncio
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from handl.routers import router, notif

load_dotenv()
TOKEN = getenv("TELEBOT_TOKEN")

dp=Dispatcher()
dp.include_router(router)

async def main():
    bot= Bot(TOKEN)
    asyncio.create_task(notif(bot))
    
    print("Bot start polling")
    await dp.start_polling(bot)

try:
    if __name__ == "__main__":
       asyncio.run(main())
except:
    print("Bot stop polling")