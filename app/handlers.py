from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from app.tosh_qaychi_qogoz import get_result

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    text = (
        "Salom, "
        "bu bot orqali bot bilan tosh-qaychi-qogoz oyini oynasangiz boladi,"
        " oynash uchun /play komandasini yuboring"
    )

    await message.answer(text=text)


@router.message(F.text == "/play")
async def play_handler(message: Message):
    text = "Quyidagilardan birini tanlang 👇"

    buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🪨 Tosh", callback_data="tosh")],
            [InlineKeyboardButton(text="✂️ Qaychi", callback_data="qaychi")],
            [InlineKeyboardButton(text="📄 Qog‘oz", callback_data="qogoz")],
        ]
    )

    await message.answer(text=text, reply_markup=buttons)


@router.callback_query(F.data.in_(["tosh", "qaychi", "qogoz"]))
async def edit_handler(query: CallbackQuery):
    # noinspection PyUnresolvedReferences
    await query.message.edit_text(text=await get_result(query))
    await query.answer()
