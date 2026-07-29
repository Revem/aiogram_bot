from aiogram import Router, F, Bot
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import aiosqlite
import asyncio


router = Router()

subcr= set()

async def notif(bot: Bot):
    while True:
        if subcr:
            for us in list(subcr):
                try:
                    await bot.send_message(us, "Hi")
                except:
                    pass
        await asyncio.sleep(10)

async def add(message):
    async with aiosqlite.connect("tgbase.sql") as bd:
        cur = await bd.cursor()
        await cur.execute("SELECT * FROM tgbase")
        result = await cur.fetchall()
        for pr in result:
            await message.answer(str(pr)[1:-1])

@router.message(Command("start"))
async def start(message: Message):
    await message.answer("/sub , /unsub, /pup")

@router.message(Command("sub"))
async def sub(message: Message):
    use_id= message.from_user.id
    subcr.add(use_id)
    await message.answer("ready")

@router.message(Command("unsub"))
async def sub(message: Message):
    use_id= message.from_user.id
    subcr.discard(use_id)
    await message.answer("ready unsub")

@router.message(Command("pup"))
async def pup(message: Message):
    if not subcr:
        await message.answer("никого")
        return
    text = "Люди\n"
    for u in subcr:
        text+=f"{u}\n"
    await message.answer(text)

@router.message(Command("base"))
async def base(message: Message):
    asyncio.create_task(add(message))
    await message.answer("ready")