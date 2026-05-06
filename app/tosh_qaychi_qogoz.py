import random

from aiogram.types import CallbackQuery

tqq = ["tosh", "qaychi", "qogoz"]


async def get_random_tqq() -> str:
    return random.choice(tqq)


async def get_result(query: CallbackQuery) -> str:
    random_tqq = await get_random_tqq()
    if query.data == "tosh":
        if random_tqq == "tosh":
            return "Durang"
        elif random_tqq == "qaychi":
            return "Yutdi"
        else:
            return "Yutqazdi"
    elif query.data == "qaychi":
        if random_tqq == "tosh":
            return "Yutqazdi"
        elif random_tqq == "qaychi":
            return "Durang"
        else:
            return "Yutdi"
    else:
        if random_tqq == "tosh":
            return "Yutdi"
        elif random_tqq == "qaychi":
            return "Yutqazdi"
        else:
            return "Durang"
