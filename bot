import asyncio, handlers, commands
from aiogram import Bot, Dispatcher

from config import TOKEN


async def main() -> None:
    bot = Bot(TOKEN)
    dp = Dispatcher()

    dp.include_routers(commands.router, handlers.router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
