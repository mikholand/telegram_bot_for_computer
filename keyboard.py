from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from buttons import *


def get_base_inline_keyboard():
	keyboard = [
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON14_SOUND], callback_data=CALLBACK_BUTTON14_SOUND),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON20_SCREEN], callback_data=CALLBACK_BUTTON20_SCREEN),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON61_MPC_FULL], callback_data=CALLBACK_BUTTON60_MPC),
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
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON60_MPC], callback_data=CALLBACK_BUTTON60_MPC),
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
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON60_MPC], callback_data=CALLBACK_BUTTON60_MPC),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON40_SYSTEM], callback_data=CALLBACK_BUTTON40_SYSTEM),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON21_SCREEN_SAVER], callback_data=CALLBACK_BUTTON21_SCREEN_SAVER),
		],
		[
			# InlineKeyboardButton(TITLES[CALLBACK_BUTTON22_MONITOR_ON], callback_data=CALLBACK_BUTTON22_MONITOR_ON),
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


def get_mpc_inline_keyboard():
	keyboard = [
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON14_SOUND], callback_data=CALLBACK_BUTTON14_SOUND),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON20_SCREEN], callback_data=CALLBACK_BUTTON20_SCREEN),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON60_MPC], callback_data=CALLBACK_BUTTON60_MPC),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON40_SYSTEM], callback_data=CALLBACK_BUTTON40_SYSTEM),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON62_MPC_PLAY], callback_data=CALLBACK_BUTTON62_MPC_PLAY),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON66_MPC_BACKWARD_SMALL],
								 callback_data=CALLBACK_BUTTON66_MPC_BACKWARD_SMALL),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON63_MPC_FORWARD_SMALL],
								 callback_data=CALLBACK_BUTTON63_MPC_FORWARD_SMALL),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON68_MPC_BACKWARD_LARGE],
								 callback_data=CALLBACK_BUTTON68_MPC_BACKWARD_LARGE),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON67_MPC_BACKWARD_MEDIUM],
								 callback_data=CALLBACK_BUTTON67_MPC_BACKWARD_MEDIUM),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON64_MPC_FORWARD_MEDIUM],
								 callback_data=CALLBACK_BUTTON64_MPC_FORWARD_MEDIUM),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON65_MPC_FORWARD_LARGE],
								 callback_data=CALLBACK_BUTTON65_MPC_FORWARD_LARGE),
		],
	]
	return InlineKeyboardMarkup(keyboard)


def get_system_inline_keyboard():
	keyboard = [
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON14_SOUND], callback_data=CALLBACK_BUTTON14_SOUND),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON20_SCREEN], callback_data=CALLBACK_BUTTON20_SCREEN),
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON60_MPC], callback_data=CALLBACK_BUTTON60_MPC),
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