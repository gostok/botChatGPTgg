from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import  InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types


def menu_kb():
    kb_list = [
        [KeyboardButton(text="Баланс")],
        [KeyboardButton(text='About')]
    ]
    kb = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True)
    return kb


def about_kb():
    kb_list = [
        [InlineKeyboardButton(text="Донат", callback_data="donat_call")],
        [InlineKeyboardButton(text="GitHub", url="https://github.com/gostok")],
        [InlineKeyboardButton(text="Сотрудничать", url="https://t.me/ateccc")]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=kb_list, resize_keyboard=True)
    return kb


def donat_kb():
    kb_list = [
        [InlineKeyboardButton(text="Прогресс",
                              web_app=types.WebAppInfo(url="https://www.donationalerts.com/widget/goal/8258259?token=xr92I07pj7TcRDTDGzl9"))],
        [InlineKeyboardButton(text="Задонатить",
                              web_app=types.WebAppInfo(url="https://www.donationalerts.com/r/square_vision_gs"))]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=kb_list, resize_keyboard=True)
    return kb


def balance_kb():
    kb_list = [
        [KeyboardButton(text="Пополнить баланс")],
        [KeyboardButton(text="История платежей")]
    ]
    kb = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True)
    return kb


def replenish_kb():
    kb_list = [
        [KeyboardButton(text="СБП")],
        [KeyboardButton(text="Картой на сайте")]
    ]
    kb = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True)
    return kb


def payment_kb(payment_type):
    kb = InlineKeyboardMarkup(row_width=3)

    prices = [
        100, 200, 300,
        400, 500, 600,
        1000, 2000, 3000
    ]

    for price in prices:
        bt = InlineKeyboardButton(text=f"{price}₽", callback_data=f"{payment_type}_{price}")
        kb.add(bt)

    return kb