# telegram_bot_for_computer
Телеграм бот для ограниченного управления компьютером

## Запуск бота
- установить Python 3.7 с [официального сайта](https://www.python.org/)
- установить Telegram Bot 12.1 с помощью команды
```
pip3 install python-telegram-bot==12.1.0
```
- подставить в `TG_TOKEN` свое значение Bot API, которое нужно получить у бота @BotFather
- скачать NirCmd с [официального сайта](http://www.nirsoft.net/utils/nircmd.html) и разместить `nircmd.exe` в папке с ботом
- скачать MultiMonitorTool с [официального сайта](https://www.nirsoft.net/utils/multi_monitor_tool.html) и разместить `MultiMonitorTool.exe` в папке с ботом
- запустить самого бота 
```
python bot.py
```

## Возможности бота
На данный момент бот умеет:
- Вкл/выкл звук
- Ставить громкость, кратное десяти (10, 20, 30, ..., 100)
- Прибавлять/убавлять громкость на 1%
- Включать заставку
- Включать/выключать экраны по отдельности и все разом
- Выключать компьютер
- Перезагружать компьютер
- Блокировать компьютер
- Заходить в меню смены пользователем

## В планах добавить:
- Управление Media Player Classic
