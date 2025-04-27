import telebot
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql+psycopg2://dbuser:pass@database:5432/dbname'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class CustomUser(Base):
    __tablename__ = 'subscription_customuser'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    tg_chat_id = Column(String)
    phone = Column(String)

Base.metadata.create_all(engine)

bot = telebot.TeleBot('8083153363:AAFLITTlPQayAY98yx724nxKaGu1844dx4A')

def contact(message):
    session = Session()
    _phone = str(message.contact.phone_number)
    _phone = _phone.replace("(", "").replace(")", "").replace("-", "").replace("+", "")
    print(_phone)

    q = session.query(CustomUser).filter(CustomUser.phone == ('+{}'.format(_phone)))
    if q.count():
        record = q.one()
        record.tg_chat_id = message.contact.user_id
        bot.send_message(message.chat.id, 'Вы успешно зарегистрировались в системе!')
        session.commit()
    else:
        bot.send_message(message.chat.id, 'Ваш номер не найден в БД')
    return None

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = telebot.types.KeyboardButton(text='Подписаться', request_contact=True)
    keyboard.add(button_phone)
    bot.send_message(message.chat.id, 'Чтобы начать работу с ботом, нажмите кнопку “Подписаться”, расположенную внизу экрана!',reply_markup=keyboard)

if __name__ == '__main__':
    print('Бот запущен')
    bot.infinity_polling()
