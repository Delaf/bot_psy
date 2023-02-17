import aiohttp
import spisok
import random
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import json

listor = spisok.list_otr


bot = Bot(token='6075264998:AAH9GaxsbnRWRsJU5og5Uanmm6RwqfOtyLw')
dp = Dispatcher(bot)

button_btc_usdt, button_eth_usdt = KeyboardButton('MAN'), KeyboardButton('WOMAN')
crypto_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
crypto_keyboard.add(button_btc_usdt, button_eth_usdt)

glob = ['odin']




async def get_price(symbol1: str = 'BTC', symbol2: str = 'USDT'):
    url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol1}{symbol2}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
    print(data)

    return json.loads(data)


def index_list1(key):
    index = 0
    nn = ""
    while index < len(listor):
        if listor[index] == key:
            nn = f'да нашли -{listor[index]}'
            break

        if index >= len(listor):
            break
        else:
            print(listor[index])
            print(f'{key} - key')
            nn = "НЕТ"
            index += 1

    return nn


def index_list2(key):
    print(f'{key}+++link2')
    nn=key
    return nn


async def get_news(key):
    print(key)
    nn = index_list2(key)
    print(nn)

    if key == "MAN":
            otvet = random.choice(list(listor.items()))
            print(f'{otvet} - otvet')
            global glob
            print(f'{glob} - #1)')

            glob.append(otvet)
            print(f'положили в глобла --- > {otvet}')
            #print(f'{glob} - смотрим что в глобале #2)')
            key=otvet
    else:
        otvet = key
        print(f'{glob} - #3)')

        #choy = random.choice(listor)

    return otvet


# чисто визуал
def pre_news(data):
    print (data.items[0]())
    #return '\n'.join(f'{key}: {value}' for key, value in data.items())
    #return '\n privet'


def get_name(otvet):
    news=otvet+"2 news to mail"
    data=(f'{news}')
    print (data)
    return data


# чисто визуал
def prepare_answer(data: dict):
    print (data.items())
    return '\n'.join(f'{key}: {value}' for key, value in data.items())
    #return '\n privet'


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hello\nWelcome to cryptocurrency price bot",
                        reply_markup=crypto_keyboard)


@dp.message_handler() #response - ответ
async def response_message(msg: types.Message):
    key = msg.text
    if key == "MAN":
        glob.clear


    otvet = await get_news(key)
    print(f'HANDLER: {glob} - #4)')

    if key == "MAN":
        old=glob[-1]; glob.clear(); glob.append(old)
        otvet=glob[-1][0]
    else:
        glob.append(key)
        otvet=f'[ {glob[-2][0]} - {glob[-1]} ] :\n\n{glob[-2][1]} - {glob[-1]}\n{glob[-2][0]} - {glob[-1]}'

    print(f'HANDLER: {glob} - #5)')

    await bot.send_message(msg.from_user.id, otvet)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

