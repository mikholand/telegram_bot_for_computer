# telegram_bot_for_computer
Телеграм бот для ограниченного управления компьютером

## Запуск бота
- установить Python 3.7 с [официального сайта](https://www.python.org/)
- установить Telegram Bot 12.1 и PyAutoGui с помощью команд
```
pip3 install python-telegram-bot==12.1.0
pip3 install pyautogui 
```
- изменить файл `config.py`
  - подставить в `TG_TOKEN` свое значение Bot API, которое нужно получить у бота @BotFather
  - подставить в `CALLBACK_USER_ID` свой Telegram User ID, который можно узнать у бота @getmyid_bot
  - изменить свой пароль в значении `password`, чтобы никто не смог случайно перезагрузить ваш компьютер (защита от дураков)
- скачать NirCmd с [официального сайта](http://www.nirsoft.net/utils/nircmd.html) и разместить `nircmd.exe` в папке с ботом
- скачать MultiMonitorTool с [официального сайта](https://www.nirsoft.net/utils/multi_monitor_tool.html) и разместить `MultiMonitorTool.exe` в папке с ботом
- запустить самого бота 
```
python bot.py
```

## Возможности бота
На данный момент бот умеет:
- Управлять громкостью
  - Вкл/выкл звук
  - Ставить громкость, кратное десяти (10, 20, 30, ..., 100)
  - Прибавлять/убавлять громкость на 1%
- Управлять экранами
  - Включать заставку
  - Включать/выключать экраны по отдельности и все разом
- Управлять питанием компьютера
  - Выключать компьютер
  - Перезагружать компьютер
  - Блокировать компьютер
  - Заходить в меню смены пользователем
- Управление Media Player Classic (горячие клавиши и шаг перемотки нужно установить в самом плеере)
  - Pause/Play
  - Перемотка назад (маленькая, средняя, большая)
  - Перемотка вперед (маленькая, средняя, большая)

## В планах добавить:
- Присылайте идеи в телеграм `@mikholand`
