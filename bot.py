import subprocess
from telegram import Bot
from telegram import Update
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CallbackQueryHandler
from telegram.utils.request import Request

TG_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

CALLBACK_BUTTON1_10 = "callback_button1_10"
CALLBACK_BUTTON2_20 = "callback_button2_20"
CALLBACK_BUTTON3_30 = "callback_button3_30"
CALLBACK_BUTTON4_40 = "callback_button4_40"
CALLBACK_BUTTON5_50 = "callback_button5_50"
CALLBACK_BUTTON6_60 = "callback_button6_60"
CALLBACK_BUTTON7_70 = "callback_button7_70"
CALLBACK_BUTTON8_80 = "callback_button8_80"
CALLBACK_BUTTON9_90 = "callback_button9_90"
CALLBACK_BUTTON10_100 = "callback_button10_100"
CALLBACK_BUTTON11_SWITCH = "callback_button11_switch"
CALLBACK_BUTTON12_INCREASE = "callback_button12_increase"
CALLBACK_BUTTON13_DECREASE = "callback_button13_decrease"
CALLBACK_BUTTON14_SOUND = "callback_button14_sound"

CALLBACK_BUTTON20_SCREEN = "callback_button20_screen"
CALLBACK_BUTTON21_SCREEN_SAVER = "callback_button21_screen_saver"
#CALLBACK_BUTTON22_MONITOR_ON = "callback_button22_monitor_on"
CALLBACK_BUTTON23_MONITOR_OFF = "callback_button23_monitor_off"
CALLBACK_BUTTON24_MONITOR2_ON = "callback_button24_monitor2_on"
CALLBACK_BUTTON25_MONITOR2_OFF = "callback_button25_monitor2_off"
CALLBACK_BUTTON26_MONITORS_ON = "callback_button26_monitors_on"
CALLBACK_BUTTON27_MONITORS_OFF = "callback_button27_monitors_off"

CALLBACK_BUTTON40_SYSTEM = "callback_button40_system"
CALLBACK_BUTTON41_SYSTEM_SHUTDOWN = "callback_button41_system_shutdown"
CALLBACK_BUTTON42_SYSTEM_REBOOT = "callback_button42_system_reboot"
CALLBACK_BUTTON43_SYSTEM_LOCKWORKSTATION = "callback_button43_system_lockworkstation"
CALLBACK_BUTTON44_SYSTEM_TSDISCON = "callback_button44_system_tsdiscon"

CALLBACK_USER = 000000000

TITLES = {
	CALLBACK_BUTTON1_10: "10%",
	CALLBACK_BUTTON2_20: "20%",
	CALLBACK_BUTTON3_30: "30%",
	CALLBACK_BUTTON4_40: "40%",
	CALLBACK_BUTTON5_50: "50%",
	CALLBACK_BUTTON6_60: "60%",
	CALLBACK_BUTTON7_70: "70%",
	CALLBACK_BUTTON8_80: "80%",
	CALLBACK_BUTTON9_90: "90%",
	CALLBACK_BUTTON10_100: "100%",
	CALLBACK_BUTTON11_SWITCH: "Вкл/выкл звук",
	CALLBACK_BUTTON12_INCREASE: "+",
	CALLBACK_BUTTON13_DECREASE: "-",
	CALLBACK_BUTTON14_SOUND: "Звук",

	CALLBACK_BUTTON20_SCREEN: "Экран",
	CALLBACK_BUTTON21_SCREEN_SAVER: "Включить заставку",
	#CALLBACK_BUTTON22_MONITOR_ON: "Включить монитор",
	CALLBACK_BUTTON23_MONITOR_OFF: "Выключить монитор",
	CALLBACK_BUTTON24_MONITOR2_ON: "Включить монитор 2",
	CALLBACK_BUTTON25_MONITOR2_OFF: "Выключить монитор 2",
	CALLBACK_BUTTON26_MONITORS_ON: "Включить все экраны",
	CALLBACK_BUTTON27_MONITORS_OFF: "Выключить все экраны",

	CALLBACK_BUTTON40_SYSTEM: "Система",
	CALLBACK_BUTTON41_SYSTEM_SHUTDOWN: "Выключить компьютер",
	CALLBACK_BUTTON42_SYSTEM_REBOOT: "Перезагрузить компьютер",
	CALLBACK_BUTTON43_SYSTEM_LOCKWORKSTATION: "Блокировать",
	CALLBACK_BUTTON44_SYSTEM_TSDISCON: "Смена пользователя",
}

def get_base_inline_keyboard():
	keyboard = [
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON14_SOUND], callback_data=CALLBACK_BUTTON14_SOUND),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON20_SCREEN], callback_data=CALLBACK_BUTTON20_SCREEN),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON40_SYSTEM], callback_data=CALLBACK_BUTTON40_SYSTEM),
		],
	]
	return InlineKeyboardMarkup(keyboard)

def get_sound_inline_keyboard():
	keyboard = [
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON14_SOUND], callback_data=CALLBACK_BUTTON14_SOUND),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON20_SCREEN], callback_data=CALLBACK_BUTTON20_SCREEN),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON40_SYSTEM], callback_data=CALLBACK_BUTTON40_SYSTEM),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON11_SWITCH], callback_data=CALLBACK_BUTTON11_SWITCH),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON1_10], callback_data=CALLBACK_BUTTON1_10),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON2_20], callback_data=CALLBACK_BUTTON2_20),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON3_30], callback_data=CALLBACK_BUTTON3_30),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON4_40], callback_data=CALLBACK_BUTTON4_40),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON5_50], callback_data=CALLBACK_BUTTON5_50),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON6_60], callback_data=CALLBACK_BUTTON6_60),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON7_70], callback_data=CALLBACK_BUTTON7_70),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON8_80], callback_data=CALLBACK_BUTTON8_80),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON9_90], callback_data=CALLBACK_BUTTON9_90),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON10_100], callback_data=CALLBACK_BUTTON10_100),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON12_INCREASE], callback_data=CALLBACK_BUTTON12_INCREASE),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON13_DECREASE], callback_data=CALLBACK_BUTTON13_DECREASE),
		],
	]
	return InlineKeyboardMarkup(keyboard)

def get_screen_inline_keyboard():
	keyboard = [
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON14_SOUND], callback_data=CALLBACK_BUTTON14_SOUND),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON20_SCREEN], callback_data=CALLBACK_BUTTON20_SCREEN),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON40_SYSTEM], callback_data=CALLBACK_BUTTON40_SYSTEM),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON21_SCREEN_SAVER], callback_data=CALLBACK_BUTTON21_SCREEN_SAVER),
		],
		[
			#InlineKeyboardButton(TITLES[CALLBACK_BUTTON22_MONITOR_ON], callback_data=CALLBACK_BUTTON22_MONITOR_ON),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON23_MONITOR_OFF], callback_data=CALLBACK_BUTTON23_MONITOR_OFF),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON24_MONITOR2_ON], callback_data=CALLBACK_BUTTON24_MONITOR2_ON),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON25_MONITOR2_OFF], callback_data=CALLBACK_BUTTON25_MONITOR2_OFF),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON26_MONITORS_ON], callback_data=CALLBACK_BUTTON26_MONITORS_ON),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON27_MONITORS_OFF], callback_data=CALLBACK_BUTTON27_MONITORS_OFF),
		],
	]
	return InlineKeyboardMarkup(keyboard)

def get_system_inline_keyboard():
	keyboard = [
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON14_SOUND], callback_data=CALLBACK_BUTTON14_SOUND),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON20_SCREEN], callback_data=CALLBACK_BUTTON20_SCREEN),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON40_SYSTEM], callback_data=CALLBACK_BUTTON40_SYSTEM),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON41_SYSTEM_SHUTDOWN],
								 callback_data=CALLBACK_BUTTON41_SYSTEM_SHUTDOWN),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON42_SYSTEM_REBOOT],
								 callback_data=CALLBACK_BUTTON42_SYSTEM_REBOOT),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON43_SYSTEM_LOCKWORKSTATION],
								 callback_data=CALLBACK_BUTTON43_SYSTEM_LOCKWORKSTATION),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON44_SYSTEM_TSDISCON],
								 callback_data=CALLBACK_BUTTON44_SYSTEM_TSDISCON),
		],
	]
	return InlineKeyboardMarkup(keyboard)

def message_handler(update: Update, context: CallbackContext):
	command = update.message.text
	print ('Got command: %s' % command)

	if  (command == '/start'):
		update.message.reply_text(text="Этот бот предназначен для удаленного управления компьютером @mikholand \n\n Интересует? Пиши в ЛС", )

	if  (command == '/keyboard'):
		update.message.reply_text(text="Добро пожаловать!", reply_markup=get_base_inline_keyboard(), )

	if  (command == '/sound'):
		update.message.reply_text(text="Панель управления звуком", reply_markup=get_sound_inline_keyboard(), )

	if  (command == '/switch_sound'):
		subprocess.Popen(switch_sound, shell=True)
		update.message.reply_text(text="Вкл/выкл звук", reply_markup=get_sound_inline_keyboard(), )

	if  (command == '/10'):
		subprocess.Popen(sound10, shell=True)
		update.message.reply_text(text="10%", reply_markup=get_sound_inline_keyboard(), )

	if  (command == '/20'):
		subprocess.Popen(sound20, shell=True)
		update.message.reply_text(text="20%", reply_markup=get_sound_inline_keyboard(), )

	if  (command == '/30'):
		subprocess.Popen(sound30, shell=True)
		update.message.reply_text(text="30%", reply_markup=get_sound_inline_keyboard(), )

	if  (command == '/40'):
		subprocess.Popen(sound40, shell=True)
		update.message.reply_text(text="40%", reply_markup=get_sound_inline_keyboard(), )

	if  (command == '/50'):
		subprocess.Popen(sound50, shell=True)
		update.message.reply_text(text="50%", reply_markup=get_sound_inline_keyboard(), )

	if  (command == '/60'):
		subprocess.Popen(sound60, shell=True)
		update.message.reply_text(text="60%", reply_markup=get_sound_inline_keyboard(), )

	if  (command == '/70'):
		subprocess.Popen(sound70, shell=True)
		update.message.reply_text(text="70%", reply_markup=get_sound_inline_keyboard(), )

	if  (command == '/80'):
		subprocess.Popen(sound80, shell=True)
		update.message.reply_text(text="80%", reply_markup=get_sound_inline_keyboard(), )

	if  (command == '/90'):
		subprocess.Popen(sound90, shell=True)
		update.message.reply_text(text="90%", reply_markup=get_sound_inline_keyboard(), )

	if  (command == '/100'):
		subprocess.Popen(sound100, shell=True)
		update.message.reply_text(text="100%", reply_markup=get_sound_inline_keyboard(), )

	if (command == '/increase'):
		subprocess.Popen(increase, shell=True)
		update.message.reply_text(text="Прибавил громкость", reply_markup=get_sound_inline_keyboard(), )
	if (command == '/decrease'):
		subprocess.Popen(decrease, shell=True)
		update.message.reply_text(text="Убавил громкость", reply_markup=get_sound_inline_keyboard(), )

	if (command == '/screen'):
		update.message.reply_text(text="Панель управления экранами", reply_markup=get_screen_inline_keyboard(), )

	if (command == '/monitor_on'):
		subprocess.Popen(monitor_on, shell=True)
		update.message.reply_text(text="Включил монитор (не работает)", reply_markup=get_screen_inline_keyboard(), )
	if (command == '/monitor_off'):
		subprocess.Popen(monitor_off, shell=True)
		update.message.reply_text(text="Выключил монитор", reply_markup=get_screen_inline_keyboard(), )

	if (command == '/monitor2_on'):
		subprocess.Popen(monitor2_on, shell=True)
		update.message.reply_text(text="Включил второй монитор", reply_markup=get_screen_inline_keyboard(), )
	if (command == '/monitor2_off'):
		subprocess.Popen(monitor2_off, shell=True)
		update.message.reply_text(text="Выключил второй монитор", reply_markup=get_screen_inline_keyboard(), )

	if (command == '/monitors_on'):
		subprocess.Popen(monitors_on, shell=True)
		update.message.reply_text(text="Включил все экраны", reply_markup=get_screen_inline_keyboard(), )
	if (command == '/monitors_off'):
		subprocess.Popen(monitors_off, shell=True)
		update.message.reply_text(text="Выключил все экраны", reply_markup=get_screen_inline_keyboard(), )

	if (command == '/system'):
		update.message.reply_text(text="Панель управления системой", reply_markup=get_system_inline_keyboard(), )

	if (command == '/shutdown xxxxxxxx'):
		subprocess.Popen(shutdown, shell=True)
		update.message.reply_text(text="Выключил компьютер", reply_markup=get_system_inline_keyboard(), )

	if (command == '/reboot xxxxxxxx'):
		subprocess.Popen(reboot, shell=True)
		update.message.reply_text(text="Перезагрузил компьютер", reply_markup=get_system_inline_keyboard(), )

	if (command == '/lock xxxxxxxx'):
		subprocess.Popen(lockworkstation, shell=True)
		update.message.reply_text(text="Заблокировал компьютер", reply_markup=get_system_inline_keyboard(), )

	if (command == '/change_user xxxxxxxx'):
		subprocess.Popen(tsdiscon, shell=True)
		update.message.reply_text(text="Вышел в меню смены пользователя", reply_markup=get_system_inline_keyboard(), )

	return

def keyboard_callback_handler(update: Update, context: CallbackContext):
	query = update.callback_query
	data = query.data
	user = query.message.chat.id

	if data == CALLBACK_BUTTON1_10:
		subprocess.Popen(sound10, shell=True)
		query.edit_message_text(
			text="10%",
			reply_markup=get_sound_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON2_20:
		subprocess.Popen(sound20, shell=True)
		query.edit_message_text(
			text="20%",
			reply_markup=get_sound_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON3_30:
		subprocess.Popen(sound30, shell=True)
		query.edit_message_text(
			text="30%",
			reply_markup=get_sound_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON4_40:
		subprocess.Popen(sound40, shell=True)
		query.edit_message_text(
			text="40%",
			reply_markup=get_sound_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON5_50:
		subprocess.Popen(sound50, shell=True)
		query.edit_message_text(
			text="50%",
			reply_markup=get_sound_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON6_60:
		subprocess.Popen(sound60, shell=True)
		query.edit_message_text(
			text="60%",
			reply_markup=get_sound_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON7_70:
		subprocess.Popen(sound70, shell=True)
		query.edit_message_text(
			text="70%",
			reply_markup=get_sound_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON8_80:
		subprocess.Popen(sound80, shell=True)
		query.edit_message_text(
			text="80%",
			reply_markup=get_sound_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON9_90:
		subprocess.Popen(sound90, shell=True)
		query.edit_message_text(
			text="90%",
			reply_markup=get_sound_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON10_100:
		subprocess.Popen(sound100, shell=True)
		query.edit_message_text(
			text="100%",
			reply_markup=get_sound_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON11_SWITCH:
		subprocess.Popen(switch_sound, shell=True)
		query.edit_message_text(
			text="Вкл/выкл звук",
			reply_markup=get_sound_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON12_INCREASE:
		subprocess.Popen(increase, shell=True)
		query.edit_message_text(
			text="Прибавил громкость",
			reply_markup=get_sound_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON13_DECREASE:
		subprocess.Popen(decrease, shell=True)
		query.edit_message_text(
			text="Убавил громкость",
			reply_markup=get_sound_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON14_SOUND:
		query.edit_message_text(
			text="Панель управления звуком",
			reply_markup=get_sound_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON20_SCREEN:
		query.edit_message_text(
			text="Панель управления экранами",
			reply_markup=get_screen_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON21_SCREEN_SAVER:
		subprocess.Popen(screen_saver, shell=True)
		query.edit_message_text(
			text="Включена заставка",
			reply_markup=get_screen_inline_keyboard(),
		)
	# elif data == CALLBACK_BUTTON22_MONITOR_ON:
	#	subprocess.Popen(monitor_on, shell=True)
	#	query.edit_message_text(
	#		text="Монитор включен",
	#		reply_markup=get_screen_inline_keyboard(),
	#	)
	elif data == CALLBACK_BUTTON23_MONITOR_OFF:
		subprocess.Popen(monitor_off, shell=True)
		query.edit_message_text(
			text="Монитор выключен",
			reply_markup=get_screen_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON24_MONITOR2_ON:
		subprocess.Popen(monitor2_on, shell=True)
		query.edit_message_text(
			text="Второй монитор включен",
			reply_markup=get_screen_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON25_MONITOR2_OFF:
		subprocess.Popen(monitor2_off, shell=True)
		query.edit_message_text(
			text="Второй монитор выключен",
			reply_markup=get_screen_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON26_MONITORS_ON:
		subprocess.Popen(monitors_on, shell=True)
		query.edit_message_text(
			text="Все экраны включены",
			reply_markup=get_screen_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON27_MONITORS_OFF:
		subprocess.Popen(monitors_off, shell=True)
		query.edit_message_text(
			text="Все экраны выключены",
			reply_markup=get_screen_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON40_SYSTEM:
		query.edit_message_text(
			text="Панель управления системой",
			reply_markup=get_system_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON41_SYSTEM_SHUTDOWN:
		if user == CALLBACK_USER:
			subprocess.Popen(shutdown, shell=True)
			query.edit_message_text(
				text="Выключил компьютер",
				reply_markup=get_system_inline_keyboard(),
			)
		else:
			query.edit_message_text(
				text="Для выключения компьютера введите следующую команду: \n\n /shutdown [password]",
				reply_markup=get_system_inline_keyboard(),
			)
	elif data == CALLBACK_BUTTON42_SYSTEM_REBOOT:
		if user == CALLBACK_USER:
			subprocess.Popen(reboot, shell=True)
			query.edit_message_text(
				text="Перезагрузил компьютер",
				reply_markup=get_system_inline_keyboard(),
			)
		else:
			query.edit_message_text(
				text="Для перезагрузки компьютера введите следующую команду: \n\n /reboot [password]",
				reply_markup=get_system_inline_keyboard(),
			)
	elif data == CALLBACK_BUTTON43_SYSTEM_LOCKWORKSTATION:
		if user == CALLBACK_USER:
			subprocess.Popen(lockworkstation, shell=True)
			query.edit_message_text(
				text="Блокировал компьютер",
				reply_markup=get_system_inline_keyboard(),
			)
		else:
			query.edit_message_text(
				text="Для блокировки компьютера введите следующую команду: \n\n /lock [password]",
				reply_markup=get_system_inline_keyboard(),
			)
	elif data == CALLBACK_BUTTON44_SYSTEM_TSDISCON:
		if user == CALLBACK_USER:
			subprocess.Popen(tsdiscon, shell=True)
			query.edit_message_text(
				text="Вышел в меню смены пользователя",
				reply_markup=get_system_inline_keyboard(),
			)
		else:
			query.edit_message_text(
				text="Для выхода в меню смены пользователя на компьютере введите следующую команду: \n\n /change_user [password]",
				reply_markup=get_system_inline_keyboard(),
			)

def main():
	print('Start')

	req = Request(
		connect_timeout=0.5,
		read_timeout=1.0,
	)
	bot = Bot(
		token=TG_TOKEN,
		request=req,
		base_url="https://telegg.ru/orig/bot",
		)
	updater = Updater(
		bot=bot,
		use_context=True,
		)

	handler = MessageHandler(Filters.all, message_handler)
	buttons_handler = CallbackQueryHandler(callback=keyboard_callback_handler)

	updater.dispatcher.add_handler(handler)
	updater.dispatcher.add_handler(buttons_handler)

	updater.start_polling()
	updater.idle()
	print('Finish')


switch_sound = 'nircmd.exe mutesysvolume 2'
sound10 = 'nircmd.exe setsysvolume 6553'
sound20 = 'nircmd.exe setsysvolume 13106'
sound30 = 'nircmd.exe setsysvolume 19659'
sound40 = 'nircmd.exe setsysvolume 26212'
sound50 = 'nircmd.exe setsysvolume 32765'
sound60 = 'nircmd.exe setsysvolume 39318'
sound70 = 'nircmd.exe setsysvolume 45871'
sound80 = 'nircmd.exe setsysvolume 52424'
sound90 = 'nircmd.exe setsysvolume 58977'
sound100 = 'nircmd.exe setsysvolume 65535'
increase = 'nircmd.exe changesysvolume 655'
decrease = 'nircmd.exe changesysvolume -655'
screen_saver = 'nircmd.exe monitor off'
monitor_on = 'MultiMonitorTool.exe /TurnOn 1'
monitor_off = 'MultiMonitorTool.exe /TurnOff 1'
monitor2_on = 'MultiMonitorTool.exe /TurnOn 5'
monitor2_off = 'MultiMonitorTool.exe /TurnOff 5'
monitors_on = 'MultiMonitorTool.exe /TurnOn 1 5'
monitors_off = 'MultiMonitorTool.exe /TurnOff 1 5'
tsdiscon = 'tsdiscon'
lockworkstation = 'rundll32.exe User32.dll,LockWorkStation'
shutdown = 'Shutdown.exe -s -t 00'
reboot = 'Shutdown.exe -r -t 00'

if __name__ == '__main__':
	main()