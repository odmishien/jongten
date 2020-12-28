import random
from mahjong.constants import EAST, WINDS, DISPLAY_WINDS

# 平和
PINFU = {
    'man': '123',
    'pin': '22567',
    'sou': '345',
    'win_tile': {'sou': '5'},
    'q': '🀚 🀚 🀇 🀈 🀉 🀝 🀞 🀟 🀒 🀓 🀔'
}

# 平和/タンヤオ
PIN_TAN = {
    'man': '234',
    'pin': '22567',
    'sou': '345',
    'win_tile': {'sou': '5'},
    'q': '🀚 🀚 🀈 🀉 🀊 🀝 🀞 🀟 🀒 🀓 🀔'
}

# 平和/タンヤオ/一盃口
PIN_TAN_IPE = {
    'man': '234234',
    'pin': '22',
    'sou': '345',
    'win_tile': {'sou': '5'},
    'q': '🀚 🀚 🀈 🀈 🀉 🀉 🀊 🀊 🀒 🀓 🀔'
}

hands = [PINFU, PIN_TAN, PIN_TAN_IPE]


def get_random_hand():
    return random.choice(hands)


def get_random_kaze_set():
    return EAST, random.choice(WINDS)


def get_is_or_not():
    return random.choice([True, False])
