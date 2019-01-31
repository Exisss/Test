from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random
import time

token = '4ba0347a24b80e5be26a0b8e4150ebd05f12ebf315b9d23ec02dba669b343b65154205edc5dcd9129b1f3'
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

print('           ##############            ')
print('        ##                ##         ')
print('      ##                    ##       ')
print('   ##                         ##     ')
print('  #  ########################## #    ')
print(' #   ##########################  #   ')
print(' #     ###                ####   #   ')
print(' #      ###              ###     #   ')
print(' #       ###            ###      #   ')
print(' #         ##          ###       #   ')
print(' #          ##       ###         #   ')
print('  ##         ##     ###        ##    ')
print('   ##             ###         ##     ')
print('    ##          ###         ##       ')
print('      ##                  ##         ')
print('         ################            ')


print('Бот запущен. \nОбработка сообщений запущена.')
while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            #print('Сообщение получено' +str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            #print('Текст: ' + event.text)
            print('+================================================================================')
            print('+ Сообщение получено в ' + str(datetime.strftime(datetime.now(),"%H:%M:%S")), 'пользователь https://vk.com/id', event.user_id)
            print('+ Текст: ' + str(event.text))
            print('+================================================================================')
            print()
            response = event.text.lower()
            if event.from_user and not (event.from_me):
                if response == "привет":
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Здравствуйте!', 'random_id': 0})
                elif response == "пока":
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'До свидания!', 'random_id': 0})
                #elif response == "КОТИКИ":
                #    attachment = get_pictures.get(vk_session, -23530818, session_api)
                #    vk_session.method('messages.send',
                #                      {'user_id': event.user_id, 'message': 'Держи котиков!', 'random_id': 0,"attachment":attachment})
