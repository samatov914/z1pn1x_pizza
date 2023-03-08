from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

inline_buttons = [ 
    InlineKeyboardButton('Отправить номер', callback_data='send_number'),
    InlineKeyboardButton('Отправить местоположение', callback_data='send_location'),
    InlineKeyboardButton('Заказать пиццу', callback_data='take_order')
]
button = InlineKeyboardMarkup().add(*inline_buttons)

number_button = [
    KeyboardButton('Подтвердить отправку номера.', request_contact=True)
]

location_button = [
    KeyboardButton('Подтвердить отправку местоположения.', request_location=True)
]

number_button = ReplyKeyboardMarkup().add(*number_button)
location_button = ReplyKeyboardMarkup().add(*location_button)
