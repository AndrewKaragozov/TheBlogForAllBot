#код написан Андреем Карагозовым. Копирование без указания автора запрещено.
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
import random
import time
from threading import Thread
import os
def check_status(s):
  if(s == 1):
    return 1
  else:
    return 2
#начало командной части
def send_message(message=None, attachment=None, keyboard=None):
  vk_session.method('messages.send', {"user_id": event.user_id, "message": message, "attachment": attachment, "keyboard": keyboard, "random_id": random.randint(-2147483648,+2147483648)})
#для ЛС

def send_chat(message=None, attachment=None):
  vk_session.method('messages.send', {"chat_id": event.chat_id, "message": message, "attachment": attachment, "random_id": random.randint(-2147483648,+2147483648)})
#для беседок

def nmap(ip):
  os.system("sudo rm home/ubuntu/results.txt")
  os.system("nmap" +ip +" -oN /home/ubuntu/results.txt")
  f = open("/home/ec2-user/results.txt", "r")
  results = f.read()
  send_message(message="Результаты сканирования: \n \n" +str(results))
#nmap

def ping(ip):
  os.system("sudo rm home/ubuntu/preresults.txt")
  os.system("ping" +ip +" -w 2 > /home/ubuntu/presults.txt")
  f = open("/home/ubuntu/presults.txt", "r")
  results = f.read()
  send_message(message="Результат: \n \n" +str(results))
#ping

def cmd(cm):
  os.system("sudo rm home/ubuntu/results.txt")
  os.system("sudo" +cm +" > /home/ubuntu/cmres.txt")
  f = open('/home/ubuntu/cmres.txt', 'r')
  result = f.read()
  send_message(message="Результат: \n \n" +str(result))
#shell

#Первая клава:

def create_key(event):
  if(str(event.user_id) in adminlist or moderlist or mains):
    keyboard = VkKeyboard(one_time = False)
  
    keyboard.add_button('Бот', color=VkKeyboardColor.DEFAULT)
    keyboard.add_button('Аптайм', color=VkKeyboardColor.DEFAULT)
  
    keyboard.add_line()          
    keyboard.add_button('Статус', color=VkKeyboardColor.DEFAULT)
    keyboard.add_button('Выкл', color=VkKeyboardColor.DEFAULT)
            
    keyboard.add_line()
    keyboard.add_button('Помощь', color=VkKeyboardColor.DEFAULT)
    
    keyboard.add_line()
    keyboard.add_button('Закрыть', color=VkKeyboardColor.DEFAULT)
  else:
    keyboard = VkKeyboard(one_time = False)
  
    keyboard.add_button('Бот', color=VkKeyboardColor.DEFAULT)
    keyboard.add_button('Аптайм', color=VkKeyboardColor.DEFAULT)
            
    keyboard.add_line()
    keyboard.add_button('Помощь', color=VkKeyboardColor.DEFAULT)
    
    keyboard.add_line()
    keyboard.add_button('Закрыть', color=VkKeyboardColor.DEFAULT)
  
  keyboard = keyboard.get_keyboard()
  return keyboard

#И еще одна:

def create_key_One(event):
  if(str(event.user_id) in adminlist or moderlist or mains):
    keyboard = VkKeyboard(one_time = True)
  
    keyboard.add_button('Бот', color=VkKeyboardColor.DEFAULT)
    keyboard.add_button('Аптайм', color=VkKeyboardColor.DEFAULT)
  
    keyboard.add_line()          
    keyboard.add_button('Статус', color=VkKeyboardColor.DEFAULT)
    keyboard.add_button('Выкл', color=VkKeyboardColor.DEFAULT)
    
    keyboard.add_line()
    keyboard.add_button('Помощь', color=VkKeyboardColor.DEFAULT)
  else:
    keyboard = VkKeyboard(one_time = True)
  
    keyboard.add_button('Бот', color=VkKeyboardColor.DEFAULT)
    keyboard.add_button('Аптайм', color=VkKeyboardColor.DEFAULT)
            
    keyboard.add_line()
    keyboard.add_button('Помощь', color=VkKeyboardColor.DEFAULT)
  
  keyboard = keyboard.get_keyboard()
  return keyboard

#И для закрытия

def close_keys():
  keyboard = VkKeyboard(one_time = True)
  return keyboard.get_empty_keyboard()
#объявили клавы

kolvo = 0
resp = ' '
mains=['CreatorsID']
adminlist=['AdminsID']
moderlist=['ModersID']
#обозначили лист создателей, админов и модеров(их id в ВК)
try:
  token = "YourGroupToken"
  vk_session = vk_api.VkApi(token = token)
  session_api = vk_session.get_api()
  longpoll = VkLongPoll(vk_session)
  start_time = time.monotonic()
except BaseException:
  print('Ошибка запуска. Проверьте настройки')
  s = 2
  exit()
#начали сессию апи ВК и запустили таймер для команды "аптайм"
print('Бот запущен!')
res = 1
#если не выдало ошибок, тогда ща пойдут логи если кто-то напишет
while(1 == 1):
  for event in longpoll.listen():
    if(event.type == VkEventType.MESSAGE_NEW):
      keyboard = create_key(event)
      OneKeyboard = create_key_One(event)
      Close = close_keys()
      response = event.text.lower()
      if(event.from_user and not event.from_me):
        kolvo = kolvo + 1
        print('Пользователь с id: ' +str(event.user_id) +" запросил: " +str(response))
        if(response == 'бот'):
          send_message(message="Бот работает исправно.", attachment="photo-184588235_457239048")
        
        elif(response == 'аптайм'):
          send_message(message='С момента запуска прошло: ' +str(int(time.monotonic() - start_time)) +' секунд', attachment='photo-184588235_457239049')
        
        elif(response == 'помощь'):
          if(str(event.user_id) in adminlist or mains):
            send_message(message='''           
            Помощь - команды бота
            Аптайм - выдаёт время с момента запуска           
            Бот - проверка работоспособности
            (add/del)moder/admin/main - добавление человека на роль
            ping [ссылка] - ping ресурса(от роли модера)
            nmap [ссылка] - nmap ресурса(от роли админа)
            Для админов:
            Статус - выдаёт статус хостинга бота и рабочую директорию
            Выкл - выключить бота
            ''', keyboard=OneKeyboard)
          else:
            send_message(message='''           
            Помощь - команды бота
            Аптайм - выдаёт время с момента запуска           
            Бот - проверка работоспособности
            (add/del)moder/admin/main - добавление человека на роль
            ping [ссылка] - ping ресурса(от роли модера)
            nmap [ссылка] - nmap ресурса(от роли админа)
            ''', keyboard=OneKeyboard)
            
        elif(response == 'начать'):
          send_message(message='Вот что я могу:', keyboard=keyboard)
          
        elif(response == 'закрыть'):
          send_message(message='&#13;', keyboard=Close)

        elif(response[0:4] == 'nmap'):
          if(str(event.user_id) in adminlist or mains):
            ip = response[4:400]
            nmap(ip)
          else:
            text = 'Недостаточно прав!'
            print(text)
            send_message(message=text)
        
        elif(response[0:4] == 'ping'):
          if(str(event.user_id) in moderlist or adminlist or mains):
            ip = response[4:400]
            ping(ip)
          else:
            text = 'Недостаточно прав!'
            print(text)
            send_message(message=text)
            
        elif(response == 'статус'):
          if(str(event.user_id) in adminlist or mains):
            dir=os.getcwd()
            stat = check_status()
            if(stat == 1):
              stat = 'OK'
            else:
              stat = 'NOT OK'
            send_message(message="Рабочая директория - " +str(dir) +'\n Статус бота - ' +stat +'\n Всего боту отправлено: ' +str(kolvo) +' сообщений')
          else:
            send_message(message='Не хватает прав!')
            
        elif(response == 'выкл'):
          if(str(event.user_id) in mains):
            send_message(message='Выключаю бота...')
            print('Выключаю бота...')
            exit() 
          else:
            send_message(message='Не хватает прав!')
            
        elif(response == 'тест'):
          send_message(message = 'Тест пройден')
          
        elif(response == 'addmain'):
          if(str(event.user_id) == '201464141'):
            send_message(message='Введите id человека в консоле')
            id = input('Введите id человека: ') 
            if(id == 'отмена'):
              text = '*karagozov (Админ) отменил добавление'
              print(text)
              send_message(message=text, attachment="photo-184588235_457239051")
            else:
              adminlist.append(id)
              text = 'Человек с id: ' +str(id) +' добавлен в список админов *karagozov (Андреем Карагозовым)'
              print(text)
              send_message(message = text, attachment = 'photo-184588235_457239050')             
          else:
            text='Недостаточно прав!'
            print(text)
            send_message(message=text)
            
        elif(response == 'addadmin'):
          if(str(event.user_id) in mains):
            send_message(message='Введите id человека в консоле')
            id = input('Введите id человека: ') 
            if(id == 'отмена'):
              text = 'Админ отменил добавление'
              print(text)
              send_message(message=text, attachment="photo-184588235_457239051")
            else:
              adminlist.append(id)
              text = 'Человек с id: ' +str(id) +' добавлен в список админов человеком с id: ' +str(event.user_id)
              print(text)
              send_message(message = text, attachment = 'photo-184588235_457239050')
          else:
            text='Недостаточно прав!'
            print(text)
            send_message(message=text)
            
        elif(response == 'addmoder'):
          if(str(event.user_id) in adminlist or moderlist):
            send_message(message='Введите id человека в консоле')
            id = input('Введите id человека: ') 
            if(id == 'отмена'):
              text = 'Админ отменил добавление'
              print(text)
              send_message(message=text, attachment="photo-184588235_457239051")
            else:
              moderlist.append(id)
              text = 'Человек с id: ' +str(id) +' добавлен в список модеров человеком с id: ' +str(event.user_id)
              print(text)
              send_message(message = text, attachment = 'photo-184588235_457239050')
          else:
            text='Недостаточно прав!'
            print(text)
            send_message(message=text)
            
        elif(response == 'delmoder'):
          if(str(event.user_id) in adminlist or moderlist):
            send_message(message='Введите id человека в консоле')
            id = input('Введите id человека: ') 
            if(id == 'отмена'):
              text = 'Админ отменил удаление'
              print(text)
              send_message(message=text, attachment="photo-184588235_457239051")
            else:
              if(id not in moderlist):
                text = 'Данного человека нет в списке модеров'
                print(text)
                send_message(message=text)
              else:
                moderlist.remove(id)
                text = 'Человек с id: ' +str(id) +' удален из списка модеров человеком с id: ' +str(event.user_id)
                print(text)
                send_message(message = text, attachment = 'photo-184588235_457239050')
          else:
            text='Недостаточно прав!'
            print(text)
            send_message(message=text)
            
        elif(response == 'deladmin'):
          if(str(event.user_id) in mains):
            send_message(message='Введите id человека в консоле')
            id = input('Введите id человека: ') 
            if(id == 'отмена'):
              text = 'Админ отменил удаление'
              print(text)
              send_message(message=text, attachment="photo-184588235_457239051")
            else:
              if(id not in adminlist):
                text = 'Данного человека нет в списке админов'
                print(text)
                send_message(message=text)
              else:
                adminlist.remove(id)
                text = 'Человек с id: ' +str(id) +' удален из списка админов человеком с id: ' +str(event.user_id)
                print(text)
                send_message(message = text, attachment = 'photo-184588235_457239050')
          else:
            text='Недостаточно прав!'
            print(text)
            send_message(message=text)
            
        elif(response == 'delmain'):
          if(str(event.user_id) == '201464141'):
            send_message(message='Введите id человека в консоле')
            id = input('Введите id человека: ') 
            if(id == 'отмена'):
              text = 'Админ отменил удаление'
              print(text)
              send_message(message=text, attachment="photo-184588235_457239051")
            else:
              if(id not in mains):
                text = 'Данного человека нет в списке создателей'
                print(text)
                send_message(message=text)
              else:
                mains.remove(id)
                text = 'Человек с id: ' +str(id) +' удален из списка создателей *karagozov (Андреем Карагозовым)'
                print(text)
                send_message(message = text, attachment = 'photo-184588235_457239050')
          else:
            text='Недостаточно прав!'
            print(text)
            send_message(message=text)
        
        elif(response[0:7] == 'команда'):
          if(str(event.user_id) in adminlist or mains):
            cm = response[7:700]
            cmd(cm)
          else:
            text='Недостаточно прав!'
            print(text)
            send_message(message=text)
            
        elif(response == 'географ'):
          send_message(message='Дьявол изгнан', attachment='photo-184588235_457239053')
            
      elif(event.from_chat and not event.from_me):
        message = input('Введите сообщение в ответ: ')
        send_chat(message=message)
