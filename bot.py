#код написан Андреем Карагозовым. Копирование без указания автора запрещено.
while(1 == 1):
  for event in longpoll.listen():
    if(event.type == VkEventType.MESSAGE_NEW):
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
            Для админов:
            Статус - выдаёт статус хостинга бота и рабочую директорию
            Выкл - выключить бота
            ''')
          else:
            send_message(message='''           
            Помощь - команды бота
            Аптайм - выдаёт время с момента запуска           
            Бот - проверка работоспособности
            (add/del)moder/admin/main - добавление человека на роль
            ''')
        elif(response == 'статус'):
          if(str(event.user_id) in adminlist or moderlist or mains):
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
#код написан Андреем Карагозовым. Копирование без указания автора запрещено.
