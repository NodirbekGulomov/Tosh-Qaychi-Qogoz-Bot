import asyncio

from app.bot import tg_bot
from app.dispatcher import dp


async def main():
    print("Bot Started ...")
    await dp.start_polling(tg_bot)


if __name__ == "__main__":
    asyncio.run(main())
