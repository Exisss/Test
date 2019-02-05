from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime, timedelta
from termcolor import colored                       #sudo apt-get install termcolor
import cowsay
import vk_api                                       #sudo apt-get install vk_api
import random

token = ''
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

login = 'none'                                      # нужен для входа "профиля админа" и получения доступа к дополнительным командам
admin = '48406925'                                  # ай-ди моего профиля ВК

#print()
#print('           ##############            ')
#print('        ##                ##         ')
#print('      ##                     ##      ')
#print('   ##                          ##    ')
#print('  #  ########################### #   ')
#print(' #    #########################  #   ')
#print(' #     ###                ####   #   ')
#print(' #      ###              ###     #   ')
#print(' #       ###            ###      #   ')
#print(' #         ##          ###       #   ')
#print(' #          ##       ###         #   ')
#print('  ##         ##     ###        ##    ')
#print('   ##             ###         ##     ')
#print('    ##          ###         ##       ')
#print('      ##                  ##         ')
#print('         ################            ')
#print()



#print(colored('\n▄▄▄▄▄▄▄▄                    ██','blue'))
#print(colored('██▀▀▀▀▀▀                    ▀▀','blue'))
#print(colored('██           ▀██  ██▀    ████        ▄▄█████▄     ▄▄█████▄','blue'))
#print(colored('███████      ████         ██        ██▄▄▄▄  ▀    ██▄▄▄▄  ▀','blue'))
#print(colored('██              ▄██▄         ██         ▀▀▀▀██▄      ▀▀▀▀██▄','blue'))
#print(colored('██▄▄▄▄▄▄   ▄█▀▀█▄   ▄▄▄██▄▄▄   █▄▄▄▄▄██    █▄▄▄▄▄██','blue'))
#print(colored('▀▀▀▀▀▀▀▀  ▀▀▀  ▀▀▀  ▀▀▀▀▀▀▀▀     ▀▀▀▀▀▀      ▀▀▀▀▀▀\n','blue'))

animal = int(random.randint(1, 14))
say = "Здравствуй, Админушка!"
if animal == 1:
    print(cowsay.cow(say))
elif animal == 2:
    print(cowsay.tux(say))
elif animal == 3:
    print(cowsay.beavis(say))
elif animal == 4:
    print(cowsay.cheese(say))
elif animal == 5:
    print(cowsay.daemon(say))
elif animal == 6:
    print(cowsay.dragon(say))
elif animal == 7:
    print(cowsay.ghostbusters(say))
elif animal == 8:
    print(cowsay.kitty(say))
elif animal == 9:
    print(cowsay.meow(say))
elif animal == 10:
    print(cowsay.milk(say))
elif animal == 11:
    print(cowsay.stegosaurus(say))
elif animal == 12:
    print(cowsay.stimpy(say))
elif animal == 13:
    print(cowsay.turkey(say))
elif animal == 14:
    print(cowsay.turtle(say))



print('============')
print('[' + colored('+','green') + ']', 'Бот запущен')
print('[' + colored('+','green') + ']', 'Обработка сообщений запущена')

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('+===============================================================================')
            print('+ Сообщение получено ' + str(event.datetime + timedelta(hours=3)), 'пользователь https://vk.com/id' + str(event.user_id))
            print('+ Текст: ' + str(event.text))
            print('+===============================================================================')
            print()
            response = event.text.lower()
            if event.from_user and not event.from_me:
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

                elif response == "!exiss" and str(event.peer_id) != str(admin):
                    message = "Вы не exiss"
                    print(colored(message, 'red'))
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': message, 'random_id': 0})

                elif response == "!exiss" and str(event.peer_id) == str(admin):
                    login = response
                    print(colored(login + ' подключён\n', 'green'))
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Exiss, добро пожаловать!', 'random_id': 0})

                elif response == "!exit" and login == "!exiss":
                    print(colored(login + ' отключён\n', 'green'))
                    login = 'none'
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Exiss, удачи!', 'random_id': 0})





