import asyncio, aioschedule
from aiogram import Bot, Router

from config import TOKEN, TestBotGroup


bot = Bot(TOKEN)
router = Router()

async def test_msg():
    await bot.send_message(TestBotGroup, 'Тестовое сообщение')

async def schedule_msg():
    aioschedule.every().day.at('16:43').do(test_msg)
    while True:
        tasks = [asyncio.create_task(job.job_func) for job in aioschedule.jobs]
        await asyncio.wait(tasks)
        await asyncio.sleep(1)