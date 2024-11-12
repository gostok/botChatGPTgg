from aiogram import Router, F, types

from routers.menu_router.menu_kb import *
from base.booking_message import *
from base.database import Database

menu_router = Router()
db = Database()


@menu_router.callback_query(F.text.startswith("donat_call"))
async def about_cmd(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('Меню Донат:', reply_markup=donat_kb())


@menu_router.message(F.text.startswith("Баланс"))
async def balance_cmd(message: types.Message):
    user_id = message.from_user.id
    await db.connect()
    balance = await db.get_user_balance(user_id)
    await message.answer(f'Баланс: {balance}₽', reply_markup=balance_kb())
    await db.close()


@menu_router.message(F.text.startswith("Пополнить баланс"))
async def replenish_cmd(message: types.Message):
    await message.answer(replenish_message, reply_markup=replenish_kb())


@menu_router.message(F.text.startswith("СБП"))
async def sbp_cmd(message: types.Message):
    await message.answer(payment_message, reply_markup=payment_kb("sbp"))


@menu_router.message(F.text.startswith("Картой на сайте"))
async def card_cmd(message: types.Message):
    await message.answer(payment_message, reply_markup=payment_kb("card"))


@menu_router.callback_query(lambda c: c.data.startswith("sbp_"))
async def process_payment(callback: types.CallbackQuery):
    price = callback.data.split("_")[1]
    payment_link = f"https://example.com/sbp_payment?amount={price}"

    await callback.answer()
    await callback.message.answer(payment_link, reply_markup=replenish_kb())


@menu_router.callback_query(lambda c: c.data.startswith("card_"))
async def process_payment(callback: types.CallbackQuery):
    price = callback.data.split("_")[1]
    payment_link = f"https://example.com/card_payment?amount={price}"

    await callback.answer()
    await callback.message.answer(payment_link, reply_markup=replenish_kb())


@menu_router.message(F.text.startswith("История платежей"))
async def history_payment_cmd(message: types.Message):
    user_id = message.from_user.id
    balance = await db.get_user_balance(user_id)
    history = await db.get_payment_history(user_id)

    hp_mes = f'Баланс: {balance}₽\n\n'
    hp_mes += f"{'ДАТА, ВРЕМЯ':<22} {'₽':<5} {'ТИП':<15}\n"
    hp_mes += "=" * 50 + "\n"

    for record in history:
        date_time = f"{record['date']} {record['time']}"
        amount = record['amount']
        type_ = record['type']
        hp_mes += f"{date_time:<22} {amount:<5} {type_:<15}\n"

    await message.answer(hp_mes)