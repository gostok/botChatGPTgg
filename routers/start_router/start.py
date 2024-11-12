from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

from base.booking_message import start_message
from routers.menu_router.menu_kb import menu_kb

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(start_message, reply_markup=menu_kb())