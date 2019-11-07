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

}

def get_sound_inline_keyboard():
	keyboard = [
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

def message_handler(update: Update, context: CallbackContext):
	command = update.message.text
	print ('Got command: %s' % command)

	if  (command == '/start'):
		update.message.reply_text(text="Этот бот предназначен для удаленного управления компьютером @mikholand \n\n Интересует? Пиши в ЛС", )

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

	return

def keyboard_callback_handler(update: Update, context: CallbackContext):
	query = update.callback_query
	data = query.data

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

if __name__ == '__main__':
	main()