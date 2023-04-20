import datetime
from sqlalchemy.exc import IntegrityError
from db_api.schemas.users import Users_base, Users_model
from db_api.schemas.bonus import Bonus_base, Bonus_model
from db_api.schemas.achievement import Achievement_base, Achievement_model
from settings import db, session


def register_user(message):
    user_id = message.from_user.id
    name = f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username if message.from_user.username else None}"
    user_level = 1
    bal_usd = 0
    bal_trx = 1
    join_date = datetime.datetime.now()
    first_referrer_id = 404
    second_referrer_id = 404
    third_referrer_id = 404
    captcha = 0
    mail = ''
    phone = ''
    wallet_trx = ''
    wallet_usdt = ''
    user_language = 'en'
    ban = 0
    patron = 0
    user = Users_base(user_id=int(user_id), name=str(name), user_level=int(user_level), bal_usd=int(bal_usd),
                 bal_trx=int(bal_trx), join_date=join_date, first_referrer_id=int(first_referrer_id),
                 second_referrer_id=int(second_referrer_id), third_referrer_id=int(third_referrer_id),
                 captcha=int(captcha), mail=str(mail), phone=str(phone), wallet_trx=str(wallet_trx),
                 wallet_usdt=str(wallet_usdt), user_language=str(user_language), ban=int(ban), patron=int(patron))
    session.add(user)
    try:
        session.commit()
        return True
    except IntegrityError:
        session.rollback()
        return False


def register_user_bonus(message):
    user_id = message.from_user.id
    daily_date = '2020-01-01 10:00:00'
    week_date = '2020-01-01 10:00:00'
    user = Bonus_base(user_id=int(user_id), daily_date=daily_date, week_date=week_date)
    session.add(user)
    try:
        session.commit()
        return True
    except IntegrityError:
        session.rollback()
        return False


def register_user_achievement(message):
    user_id = message.from_user.id
    daily_bonus = 0
    c_daily_bonus = 0
    week_bonus = 0
    c_week_bonus = 0
    pay_trx = 0
    c_pay_trx = 0
    pay_trx_th = 0
    c_pay_trx_th = 0
    game_dice = 0
    c_game_dice = 0
    game_mine = 0
    c_game_mine = 0
    game_fifty = 0
    c_game_fifty = 0
    game_case = 0
    c_game_case = 0
    game_slot = 0
    c_game_slot = 0
    game_num = 0
    c_game_num = 0
    game_num_win_hun = 0
    c_game_num_win_hun = 0
    win_lot = 0
    c_win_lot = 0
    c_f_ref = 0
    c_s_ref = 0
    c_a_ref = 0
    user = Achievement_base(user_id=int(user_id), daily_bonus=daily_bonus, c_daily_bonus=c_daily_bonus, week_bonus=week_bonus,
                      c_week_bonus=c_week_bonus, pay_trx=pay_trx, c_pay_trx=c_pay_trx, pay_trx_th=pay_trx_th,
                      c_pay_trx_th=c_pay_trx_th, game_dice=game_dice, c_game_dice=c_game_dice, game_mine=game_mine,
                      c_game_mine=c_game_mine, game_fifty=game_fifty, c_game_fifty=c_game_fifty, game_case=game_case,
                      c_game_case=c_game_case, game_slot=game_slot, c_game_slot=c_game_slot, game_num=game_num,
                      c_game_num=c_game_num, game_num_win_hun=game_num_win_hun, c_game_num_win_hun=c_game_num_win_hun,
                      win_lot=win_lot, c_win_lot=c_win_lot, c_f_ref=c_f_ref, c_s_ref=c_s_ref, c_a_ref=c_a_ref)
    session.add(user)
    try:
        session.commit()
        return True
    except IntegrityError:
        session.rollback()
        return False


async def select_all_users():
    users = await Users_model.query.gino.all()
    return users


async def count_users():
    count = await db.func.count(Users_model.user_id).gino.scalar()
    return count


async def select_user(user_id):
    user = await Users_model.query.where(Users_model.user_id == user_id).gino.first()
    return user


async def select_user_bonus(user_id):
    bonus = await Bonus_model.query.where(Bonus_model.user_id == user_id).gino.first()
    return bonus


async def select_user_achievement(user_id):
    achievement = await Achievement_model.query.where(Achievement_model.user_id == user_id).gino.first()
    return achievement


async def give_bonus_ref(user_id):
    """Pеферальний бонус"""
    await Users_model.update.values(bal_trx=Users_model.bal_trx + 1).where(Users_model.user_id == user_id).gino.status()
    session.commit()

async def give_bonus_sec_ref(user_id):
    """Pеферальний бонус 2 рівень"""
    await Users_model.update.values(bal_trx=Users_model.bal_trx + 0.5).where(Users_model.user_id == user_id).gino.status()
    session.commit()

async def give_bonus_thi_ref(user_id):
    """Pеферальний бонус 3 рівень"""
    await Users_model.update.values(bal_trx=Users_model.bal_trx + 0.2).where(Users_model.user_id == user_id).gino.status()
    session.commit()

class DBCommands_middleware:
    async def get_user(self, user_id):
        user = await Users_model.query.where(Users_model.user_id == user_id).gino.first()
        return user