from util import get_random_kaze_set, get_is_or_not
from questions import questions
import random
from mahjong.hand_calculating.hand import HandCalculator
from mahjong.tile import TilesConverter
from mahjong.hand_calculating.hand_config import HandConfig
from mahjong.constants import DISPLAY_WINDS

calculator = HandCalculator()


def main():
    hand = random.choice(questions)
    round_wind, player_wind = get_random_kaze_set()
    tiles = TilesConverter.string_to_136_array(
        man=hand.get_man(), pin=hand.get_pin(), sou=hand.get_sou())
    win_tile = TilesConverter.string_to_136_array(
        **hand.get_win_tile())[0]
    conf = {
        'is_tsumo': get_is_or_not(),
        'is_riichi': get_is_or_not(),
        'player_wind': player_wind,
        'round_wind': round_wind
    }
    config = HandConfig(**conf)
    result = calculator.estimate_hand_value(tiles, win_tile, config=config)

    question_caption = ''
    if conf['is_tsumo']:
        question_caption += f"ツモ {hand.get_win_tile()} "
    else:
        question_caption += f"ロン {hand.get_win_tile()} "

    if conf['is_riichi']:
        question_caption += 'リーチ有 '
    question_caption += f"場風: {DISPLAY_WINDS[conf['round_wind']]} 自風: {DISPLAY_WINDS[conf['player_wind']]}"

    print(hand.get_figure())
    print(question_caption)
    client_answer = input().split(',')
    if int(client_answer[0]) == result.cost['main'] and int(client_answer[1]) == result.cost['additional']:
        print('正解!!')
    else:
        print(f"不正解!! 正解は {result.cost['main']}, {result.cost['additional']}")


if __name__ == "__main__":
    main()
