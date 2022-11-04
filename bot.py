import subprocess
import pyautogui
from telegram import Bot, Update
from telegram.ext import CallbackContext, Updater, MessageHandler, Filters, CallbackQueryHandler
from telegram.utils.request import Request
from config import *
from keyboard import *


def message_handler(update: Update, context: CallbackContext):
	command = update.message.text
	print('Got command: %s' % command)

	if (command == '/start'):
		update.message.reply_text(
			text="Этот бот предназначен для удаленного управления компьютером @mikholand \n\n Интересует? Пиши в ЛС", )

	if (command == '/keyboard'):
		update.message.reply_text(text="Добро пожаловать!", reply_markup=get_base_inline_keyboard(), )

	if (command == '/sound'):
		update.message.reply_text(text="Панель управления звуком", reply_markup=get_sound_inline_keyboard(), )

	if (command == '/switch_sound'):
		subprocess.Popen(switch_sound, shell=True)
		update.message.reply_text(text="Вкл/выкл звук", reply_markup=get_sound_inline_keyboard(), )

	if (command == '/10'):
		subprocess.Popen(sound10, shell=True)
		update.message.reply_text(text="10%", reply_markup=get_sound_inline_keyboard(), )

	if (command == '/20'):
		subprocess.Popen(sound20, shell=True)
		update.message.reply_text(text="20%", reply_markup=get_sound_inline_keyboard(), )

	if (command == '/30'):
		subprocess.Popen(sound30, shell=True)
		update.message.reply_text(text="30%", reply_markup=get_sound_inline_keyboard(), )

	if (command == '/40'):
		subprocess.Popen(sound40, shell=True)
		update.message.reply_text(text="40%", reply_markup=get_sound_inline_keyboard(), )

	if (command == '/50'):
		subprocess.Popen(sound50, shell=True)
		update.message.reply_text(text="50%", reply_markup=get_sound_inline_keyboard(), )

	if (command == '/60'):
		subprocess.Popen(sound60, shell=True)
		update.message.reply_text(text="60%", reply_markup=get_sound_inline_keyboard(), )

	if (command == '/70'):
		subprocess.Popen(sound70, shell=True)
		update.message.reply_text(text="70%", reply_markup=get_sound_inline_keyboard(), )

	if (command == '/80'):
		subprocess.Popen(sound80, shell=True)
		update.message.reply_text(text="80%", reply_markup=get_sound_inline_keyboard(), )

	if (command == '/90'):
		subprocess.Popen(sound90, shell=True)
		update.message.reply_text(text="90%", reply_markup=get_sound_inline_keyboard(), )

	if (command == '/100'):
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

	if (command == '/shutdown ' + password):
		subprocess.Popen(shutdown, shell=True)
		update.message.reply_text(text="Выключил компьютер", reply_markup=get_system_inline_keyboard(), )

	if (command == '/reboot ' + password):
		subprocess.Popen(reboot, shell=True)
		update.message.reply_text(text="Перезагрузил компьютер", reply_markup=get_system_inline_keyboard(), )

	if (command == '/lock ' + password):
		subprocess.Popen(lockworkstation, shell=True)
		update.message.reply_text(text="Заблокировал компьютер", reply_markup=get_system_inline_keyboard(), )

	if (command == '/change_user ' + password):
		subprocess.Popen(tsdiscon, shell=True)
		update.message.reply_text(text="Вышел в меню смены пользователя", reply_markup=get_system_inline_keyboard(), )

	if (command == '/mpc'):
		update.message.reply_text(text="Панель управления Media Player Classic",
								  reply_markup=get_mpc_inline_keyboard(), )

	if (command == '/pause'):
		pyautogui.typewrite(' ')
		update.message.reply_text(text="Pause/Play", reply_markup=get_mpc_inline_keyboard(), )
	if (command == '/play'):
		pyautogui.typewrite(' ')
		update.message.reply_text(text="Pause/Play", reply_markup=get_mpc_inline_keyboard(), )

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
		if user == CALLBACK_USER_ID:
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
		if user == CALLBACK_USER_ID:
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
		if user == CALLBACK_USER_ID:
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
		if user == CALLBACK_USER_ID:
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
	elif data == CALLBACK_BUTTON60_MPC:
		query.edit_message_text(
			text="Панель управления Media Player Classic",
			reply_markup=get_mpc_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON62_MPC_PLAY:
		pyautogui.typewrite(' ')
		query.edit_message_text(
			text="Pause/Play",
			reply_markup=get_mpc_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON63_MPC_FORWARD_SMALL:
		pyautogui.keyDown('right')
		pyautogui.keyUp('right')
		query.edit_message_text(
			text=">",
			reply_markup=get_mpc_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON64_MPC_FORWARD_MEDIUM:
		pyautogui.keyDown('ctrl')
		pyautogui.keyDown('right')
		pyautogui.keyUp('right')
		pyautogui.keyUp('ctrl')
		query.edit_message_text(
			text=">>",
			reply_markup=get_mpc_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON65_MPC_FORWARD_LARGE:
		pyautogui.keyDown('alt')
		pyautogui.keyDown('right')
		pyautogui.keyUp('right')
		pyautogui.keyUp('alt')
		query.edit_message_text(
			text=">>>",
			reply_markup=get_mpc_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON66_MPC_BACKWARD_SMALL:
		pyautogui.keyDown('left')
		pyautogui.keyUp('left')
		query.edit_message_text(
			text="<",
			reply_markup=get_mpc_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON67_MPC_BACKWARD_MEDIUM:
		pyautogui.keyDown('ctrl')
		pyautogui.keyDown('left')
		pyautogui.keyUp('left')
		pyautogui.keyUp('ctrl')
		query.edit_message_text(
			text="<<",
			reply_markup=get_mpc_inline_keyboard(),
		)
	elif data == CALLBACK_BUTTON68_MPC_BACKWARD_LARGE:
		pyautogui.keyDown('alt')
		pyautogui.keyDown('left')
		pyautogui.keyUp('left')
		pyautogui.keyUp('alt')
		query.edit_message_text(
			text="<<<",
			reply_markup=get_mpc_inline_keyboard(),
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
		#base_url="https://telegg.ru/orig/bot", # proxy для работы в РФ
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



if __name__ == '__main__':
	main()
