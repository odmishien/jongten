import random
from mahjong.constants import EAST, WINDS, DISPLAY_WINDS


def get_random_kaze_set():
    return EAST, random.choice(WINDS)


def get_is_or_not():
    return random.choice([True, False])
