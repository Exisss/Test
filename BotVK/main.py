from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime, timedelta
from termcolor import colored
import vk_api
import random
import time


token = ''
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

login = 'none'
admin = '48406925'

print()
print('           ##############            ')
print('        ##                ##         ')
print('      ##                     ##      ')
print('   ##                          ##    ')
print('  #  ########################### #   ')
print(' #    #########################  #   ')
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
print()

print('============')
print('[' + colored('+','green') + ']', 'Бот запущен')
print('[' + colored('+','green') + ']', 'Обработка сообщений запущена')
#print('*Бот запущен. \n*Обработка сообщений запущена.')


while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('+===============================================================================')
            print('+ Сообщение получено ' + str(event.datetime + timedelta(hours=3)), 'пользователь https://vk.com/id' + str(event.user_id))
            print('+ Текст: ' + str(event.text))
            print('+', event.peer_id)
            print('+===============================================================================')
            print()
            response = event.text.lower()
            if event.from_user and not (event.from_me):
                if response == "привет" or response == "здравствуйте" or response == "прив":
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Здравствуйте!', 'random_id': 0})
                elif response == "пока" or response == "досвидания" or response == "до свидания" or response == "поки":
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'До свидания!', 'random_id': 0})
                elif response == "инфо" or response == "info" or response == "информация":
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'BotVK v20190201\n Интеллектуальная собственность Чибисова С.С.{https://vk.com/id48406925}', 'random_id': 0})

                elif response == "help" or response == "помощь" or response == "/help" or response == "команды":
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'BotVK v20190201 \nКоманды: \n1) привет \n2) пока\n3) инфо - информация о боте', 'random_id': 0})


#======================================   СПЕЦИАЛЬНЫЕ КОМАНДЫ   ====================================================================

                elif response == "!exiss" and str(event.peer_id) == str(admin) and login == response:
                    print(colored('Вы уже авторизовались', 'red'))
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Вы уже авторизовались', 'random_id': 0})

                elif response == "!exiss" and str(event.peer_id) == str(admin):
                    login = response
                    print(colored(login + ' подключён\n', 'green'))
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Exiss, добро пожаловать!', 'random_id': 0})

                elif response == "!ls" and str(event.peer_id) == str(admin):
                    print(colored(response, yellow))
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Exiss, вот Лог-файл с сервера.', 'random_id': 0})
                    vk_session.method('docs.getMessagesUploadServer',
                                      {'peer_id': event.peer_id, 'document': 'logging', 'random_id': 0})

                elif response == "!exit" and login == "!exiss":
                    print(colored(login + ' отключён\n', 'green'))
                    login = 'none'
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Exiss, удачи!', 'random_id': 0})





