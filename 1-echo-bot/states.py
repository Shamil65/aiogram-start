from aiogram.fsm.state import StatesGroup, State

# FSM состояния для регистрации
class Reg(StatesGroup):
    name = State()   # Ожидание имени
    phone = State()  # Ожидание телефона