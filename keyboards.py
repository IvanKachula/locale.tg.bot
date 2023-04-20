import random
from config import _
from aiogram import types


markup_select_language = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
ukrainian = types.KeyboardButton('🇺🇦 Українська')
russian = types.KeyboardButton('🇷🇺 Русский')
english = types.KeyboardButton('🇬🇧 English')
markup_select_language.add(ukrainian, russian, english)

markup_captcha = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
captcha_true = types.KeyboardButton(f'633912')
captcha_false_q = types.KeyboardButton(f'{random.randint(100000, 999999)}')
captcha_false_w = types.KeyboardButton(f'{random.randint(100000, 999999)}')
captcha_false_r = types.KeyboardButton(f'{random.randint(100000, 999999)}')
captcha_false_t = types.KeyboardButton(f'{random.randint(100000, 999999)}')
captcha_false_y = types.KeyboardButton(f'{random.randint(100000, 999999)}')
captcha_false_a = types.KeyboardButton(f'{random.randint(100000, 999999)}')
captcha_false_s = types.KeyboardButton(f'{random.randint(100000, 999999)}')
captcha_false_d = types.KeyboardButton(f'{random.randint(100000, 999999)}')
return_captcha = types.KeyboardButton(_('Ввести іншу пошту'))
markup_captcha.add(captcha_true, captcha_false_q, captcha_false_w, captcha_false_r, captcha_false_t, captcha_false_y, captcha_false_a, captcha_false_s, captcha_false_d).add(return_captcha)


markup_phone = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
phone_num = types.KeyboardButton(_("📱 Поділитись номером"), request_contact=True)
markup_phone.add(phone_num)


markup_start = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
earn = types.KeyboardButton(_('🎯 Ігри 🎮'))
stat = types.KeyboardButton(_('📊 Статистика TRON'))
sos = types.KeyboardButton(_('🆘 Тех. Підтримка'))
ad = types.KeyboardButton(_('📱 Рекламний кабінет'))
cabinet = types.KeyboardButton(_('📳 Мій кабінет'))
bonus = types.KeyboardButton(_('🎁 BONUS'))
donation = types.KeyboardButton(_('❤ Підтримати бота'))
more_trx = types.KeyboardButton(_('🤑 Отримати до 1.000 TRX'))
achivments = types.KeyboardButton(_('🏆 Досягнення'))
say_hi = types.KeyboardButton(_('🗣 Поділитись історією/музикою'))
patreon = types.KeyboardButton(_('🅿 Наш Patreon and 🅱 Boosty'))
ref = types.KeyboardButton(_('👤 Партнерська програма'))
markup_start.add(earn).row(cabinet, ref).row(bonus, achivments).row(stat, more_trx).add(say_hi).add(donation).add(patreon).add(ad, sos)


markup_change_language = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=3)
ukrainian = types.InlineKeyboardButton('🇺🇦 Українська', callback_data="ua_lang")
russian = types.InlineKeyboardButton('🇷🇺 Русский', callback_data="ru_lang")
english = types.InlineKeyboardButton('🇬🇧 English', callback_data="en_lang")
markup_change_language.add(ukrainian, russian, english)

