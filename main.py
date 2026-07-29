import asyncio
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from handl.routers import router, notif
from aiohttp import web
import threading
import os

load_dotenv()
TOKEN = getenv("TELEBOT_TOKEN")

dp=Dispatcher()
dp.include_router(router)

async def handle_health(request):
    """Просто отвечаем, что живы, чтобы Render не убил процесс"""
    return web.Response(text="I'm alive!", status=200)

async def run_web_server():
    """Запускаем веб-сервер на порту, который даёт Render"""
    app = web.Application()
    app.router.add_get('/', handle_health)
    
    # Render даёт порт через переменную PORT, по умолчанию 10000
    port = int(os.environ.get('PORT', 10000))
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"✅ Веб-сервер запущен на порту {port}")
    
    # Держим сервер запущенным бесконечно
    await asyncio.Event().wait()

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