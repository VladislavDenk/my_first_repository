"""Неэффективный асинхронный код"""

# import asyncio
# import time


# async def send_mail(num):
#     print(f"Улетело сообщение {num}")
#     await asyncio.sleep(1)  # Имитация отправки сообщения по сети
#     print(f"Сообщение {num} доставлено")


# async def main():
#     for i in range(10):
#         await send_mail(i) # Ждём результата выполнения очередной корутины "send_mail"


# start_time = time.time()
# asyncio.run(main())
# print(f"Время выполнения программы: {time.time() - start_time} c")

"""Блокирующий асинхронный код"""

# import time
# from datetime import datetime

# # ...

# async def every_hour_notification(bot: Bot):
#     while True:
#         current_time = datetime.now()
#         if current_time.minute == 0:
#             await bot.send_message(
#                 chat_id=OWNER_CHAT_ID,
#                 text=f'Сейчас ровно {current_time.hour} ч.!'
#             )
#             await asyncio.sleep(60) # Ждём минуту, чтобы не повторяться в одном и том же часу
#         else:
#             await asyncio.sleep(1)


# async def main():

#     # ...

#     bot = Bot()
#     dp = Dispatcher()

#     # ...
#     # Новичок добавляет вызов функции `every_hour_notification` либо здесь и до поллинга дело не доходит
#     # await every_hour_notification(bot)

#     await dp.start_polling(bot)

#     # Либо здесь и тогда дело не доходит уже до функции `every_hour_notification`
#     # await every_hour_notification(bot)

"""Одновременный запуск 10 корутин"""

# import asyncio
# import time

# async def send_mail(num):
#     print(f'Улетело сообщение {num}')
#     await asyncio.sleep(1)
#     print(f'Сообщение {num} доставлено')

# async def main():
#     tasks = [send_mail(i) for i in range(10)]
#     await asyncio.gather(*tasks)


# start_time = time.time()
# asyncio.run(main())
# print(f'Время выполнения программы: {time.time() - start_time} с')

"""Работа с API с помощью библиотеки requests"""

"""
Давайте выясним где прямо сейчас находится 
Международная Космическая Станция.
"""

# import requests


# api_url = 'http://api.open-notify.org/iss-now.json'

# response = requests.get(api_url) # Отправляем GET-запрос и сохраняем ответ в переменной response

# if response.status_code == 200: # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
#     print(response.text)
# else:
#     print(response.status_code) # При другом коде ответа выводим этот код

"""
Запрос к API для числа 43
"""
# import requests

# api_url = 'http://numbersapi.com/43'

# responce = requests.get(api_url) # Отправляем GET-запрос и сохраняем ответ в переменной responce

# if responce.status_code == 200:
#     print(responce.text)
# else:
#     print(responce.status_code)

"""Автоматизируем запросы к Telegram Bot API"""

# import requests
# import time


# API_URL = 'https://api.telegram.org/bot'
# API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
# BOT_TOKEN = '7666593401:AAH5gIRQUlmD3PHCIxsUgpQd5TDu_ignouk'
# ERROR_TEXT = 'Здесь должна была быть картинка с котиком :('

# offset = -2
# counter = 0
# cat_response: requests.Response
# cat_link: str

# while counter < 100:

#     print('attempt =', counter) #Чтобы видеть в консоли, что код живет

#     updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

#     if updates['result']:
#         for result in updates['result']:
#             offset = result['update_id']
#             chat_id = result['message']['from']['id']
#             cat_response = requests.get(API_CATS_URL)
#             if cat_response.status_code == 200:
#                 cat_link = cat_response.json()[0]['url']
#                 requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
#             else:
#                 requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

#     time.sleep(1)
#     counter += 1

"""POLLING"""

# import requests
# import time

# API_URL = 'https://api.telegram.org/bot'
# BOT_TOKEN = '7666593401:AAH5gIRQUlmD3PHCIxsUgpQd5TDu_ignouk'

# offset = -2
# updates: dict


# def do_something() -> None:
#     print('Был апдейт')


# while True:
#     start_time = time.time()
#     updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

#     if updates['result']:
#         for result in updates['result']:
#             offset = result['update_id']
#             do_something()

#     time.sleep(3)
#     end_time = time.time()
#     print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')

"""Long polling"""

# import requests
# import time

# API_URL = 'https://api.telegram.org/bot'
# BOT_TOKEN = '7666593401:AAH5gIRQUlmD3PHCIxsUgpQd5TDu_ignouk'
# offset = -2
# timeout = 60
# updates: dict

# def do_something() -> None:
#     print('Был апдейт')


# while True:
#     start_time = time.time()
#     updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

#     if updates['result']:
#         for result in updates['result']:
#             offset = result['update_id']
#             do_something()

#     end_time = time.time()
#     print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')